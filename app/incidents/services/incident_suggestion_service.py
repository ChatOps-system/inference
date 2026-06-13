from fastapi import HTTPException
from instructor.core import InstructorRetryException
from pydantic import ValidationError
from app.ai.services.instructor_service import InstructorService
from app.incidents.responses.generate_incident_suggestion_response import GenerateIncidentSuggestionResponse

class IncidentSuggestionService:
    def __init__(self):
        self.instructor_service = InstructorService()

    def generate_incident_suggestion(self, message: str):
        try:
            incident_suggestion = self.instructor_service.generate_incident_suggestion(message)
            return GenerateIncidentSuggestionResponse(
                incidentSuggestion= incident_suggestion,
                message= f"Generated Incident suggestion successfully for message: {message}",
            )
        except ValidationError as e:
            raise HTTPException(
                status_code=422,
                detail={
                    "error": "Invalid model output",
                    "details": str(e)
                }
            )
        except InstructorRetryException as e:
            raise HTTPException(
                status_code=422,
                detail={
                    "error": "Model validation failed after retries",
                    "details": str(e)
                }
            )
        except Exception as e:
            raise HTTPException(
                status_code=503,
                detail={
                    "error": "Generate incident suggestion failed",
                    "details": str(e)
                }
            )    
