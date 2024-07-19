from pydantic import BaseModel, Field
from typing import List


class ZeroShotClassifierRequest(BaseModel):
    text: str = Field(title="Input Text", min_length=10, max_length=640)
    labels: List[str] = Field(title="List of Candidate Labels")


class ZeroShotClassifierResponse(BaseModel):
    labels: List[str] = Field(title="List of Candidate Labels")
    scores: List[float] = Field(title="List of Scores corresponding to each label")

    class Config:
        extra = "ignore"