from typing import List

from pydantic import BaseModel, Field


class ZeroShotClassifierRequest(BaseModel):
    """
    Request Model that contain the data for sending
    a request to the API server.

    Arguments:
        - `text`: The text that has to be classified
        - `labels`: Candidate labels for classification
    """
    text: str = Field(min_length=10, max_length=640)
    labels: List[str]


class ZeroShotClassifierResponse(BaseModel):
    """
    Response Model for the the text classifier
    """
    labels: List[str]
    scores: List[float]

    class Config:
        extra = "ignore"
