import os
from contextlib import asynccontextmanager

import gradio as gr
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.requests import Request
from optimum.onnxruntime import ORTModelForSequenceClassification
from optimum.pipelines import pipeline
from transformers import AutoTokenizer

from api.middleware import ResponseID, ResponseTime
from api.models import ZeroShotClassifierRequest, ZeroShotClassifierResponse
from webapp.gradio_app import app


@asynccontextmanager
async def lifespan(_server: FastAPI):
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


server = FastAPI(
    lifespan=lifespan,
    title="Zero Shot Text Classification",
    description=f"Huggingface Model: {os.getenv('HF_MODEL')}"
)

server.add_middleware(ResponseTime)
server.add_middleware(ResponseID)

@server.get("/")
async def root():
    return RedirectResponse("/gradio")


@server.post("/predict", response_model=ZeroShotClassifierResponse)
async def predict(request: Request, params: ZeroShotClassifierRequest):
    # retrieve the pipeline and process the text
    return request.state.model(params.text, candidate_labels=params.labels)


server = gr.mount_gradio_app(server, app, path="/gradio")