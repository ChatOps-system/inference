import random
from app.ai.schemas.classifier_prediction_schema import ClassifierPrediction


class ClassifierService:
    def __init__(self):
        ...
    def predict(self, message: str)-> ClassifierPrediction:
        return ClassifierPrediction(
            isIncident=random.choice([True,False]),
            confidence=round(random.uniform(0.5,0.99),2)
        )