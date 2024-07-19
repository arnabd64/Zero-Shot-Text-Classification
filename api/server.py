import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.requests import Request
from optimum.onnxruntime import ORTModelForSequenceClassification
from optimum.pipelines import pipeline
from transformers import AutoTokenizer, ZeroShotClassificationPipeline
from api.models import ZeroShotClassifierRequest, ZeroShotClassifierResponse


@asynccontextmanager
async def lifespan(_app: FastAPI):
    # load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(os.getenv("HF_MODEL"))

    # load model
    model = ORTModelForSequenceClassification.from_pretrained(os.getenv("HF_MODEL"))

    # build classification pipeline
    classifier = pipeline(
        task='zero-shot-classification',
        tokenizer=tokenizer,
        model=model
    )
    # send the model to API state
    yield {"model": classifier}


app = FastAPI(
    lifespan=lifespan,
    title="Zero Shot Text Classification",
    description=f"Huggingface Model: {os.getenv('HF_MODEL')}"
)

@app.get("/")
async def root():
    return {"message": "Server is Running"}


@app.post("/predict", response_model=ZeroShotClassifierResponse)
async def predict(request: Request, params: ZeroShotClassifierRequest):
    # retrieve the pipeline
    classifier = request.state.model

    # process the text
    response = classifier(params.text, candidate_labels=params.labels)

    return response