import os

from optimum.onnxruntime import ORTModelForSequenceClassification
from optimum.pipelines import pipeline
from transformers import AutoTokenizer


class Classifier:
    
    def __init__(self):
        self._hf_model_id = os.getenv("HF_MODEL")
        _tokenizer = AutoTokenizer.from_pretrained(self._hf_model_id)
        _model = ORTModelForSequenceClassification.from_pretrained(self._hf_model_id)
        self.pipeline = pipeline(
            task="zero-shot-classification",
            tokenizer=_tokenizer,
            model=_model
        )
        
    def classify(self, text: str, labels: list[str]) -> dict:
        response = self.pipeline(text, labels)
        return response
    
    def webui(self, text: str, labels: str) -> dict[str, float]:
        labels = labels.split(",")
        response = self.classify(text, labels)
        labels, scores = response["labels"], response['scores']
        return {label: score for label, score in zip(labels, scores)}
