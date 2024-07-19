import os

from optimum.onnxruntime import ORTModelForSequenceClassification
from optimum.pipelines import pipeline
from transformers import AutoTokenizer

classifier = pipeline(
    task="zero-shot-classification",
    tokenizer=AutoTokenizer.from_pretrained(os.getenv("HF_MODEL")),
    model=ORTModelForSequenceClassification.from_pretrained(os.getenv("HF_MODEL"))
)

def classify(text: str, labels: str):
    labels = labels.split(",")
    response = classifier(text, labels)
    labels, scores = response["labels"], response['scores']
    return {label: score for label, score in zip(labels, scores)}