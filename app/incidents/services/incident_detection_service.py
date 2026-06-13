from app.ai.services.classifier_service import ClassifierService
from app.incidents.responses.detect_incident_response import DetectIncidentResponse
class IncidentDetectionService:
    def __init__(self):
        self.classifier_service = ClassifierService()
    def detect_incident(self, message: str):
        prediction = self.classifier_service.predict(message)
        return DetectIncidentResponse(
            isIncident=prediction.isIncident,
            confidence=prediction.confidence,
            message=f"Detected incident for message: {message}"
        )
