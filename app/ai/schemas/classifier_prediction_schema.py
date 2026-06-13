from pydantic import BaseModel

class ClassifierPrediction(BaseModel):
    isIncident: bool
    confidence: float