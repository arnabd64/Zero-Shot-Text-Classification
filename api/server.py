from typing import Annotated, List

import gradio as gr
from fastapi import Body, FastAPI
from fastapi.responses import RedirectResponse

from api.middleware import ResponseID, ResponseTime
from handler.inference import Classifier
from webapp.gradio_app import app

classifier = Classifier()


server = FastAPI(
    title="Zero Shot Text Classification",
    description=f"Huggingface Model: {classifier._hf_model_id}"
)

server.add_middleware(ResponseTime)
server.add_middleware(ResponseID)

@server.get("/")
async def root():
    return RedirectResponse("/gradio")


@server.post("/predict")
async def predict(text: Annotated[str, Body()], labels: Annotated[List[str], Body()]):
    return classifier.classify(text, labels)


server = gr.mount_gradio_app(server, app, path="/gradio")