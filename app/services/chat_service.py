from fastapi import HTTPException
from pydantic import ValidationError

from app.models.draft_generator_model import DraftGeneratorModel
from app.schemas.detect_incident_response import DetectIncidentResponse
from app.schemas.generate_incident_draft_response import GenerateIncidentDraftResponse

class ChatService:
    def __init__(self, draftGeneratorModel: DraftGeneratorModel):
        self.draftGeneratorModel = draftGeneratorModel

    def generate_incident_draft(self, message: str):
        try:
            incident_draft = self.draftGeneratorModel.generate(message)
            return GenerateIncidentDraftResponse(
                incident_draft= incident_draft,
                message= f"Generated Incident draft successfully for message: {message}",
            )
        except ValidationError as e:
            raise HTTPException(
                status_code=422,
                detail={
                    "error": "Invalid model output",
                    "message": message,
                    "details": str(e)
                }
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail={
                    "error": "Model generation failed",
                    "message": message,
                    "details": str(e)
                }
            )    
    def detect_incident(self, message: str):        
        return DetectIncidentResponse(
            isIncident=True,
            confidence=0.8,
            message=f"Detected incident for message: {message}"
        )
