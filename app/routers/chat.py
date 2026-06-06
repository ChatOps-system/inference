from fastapi import APIRouter
from app.config import settings
from app.models.generic_draft_generator_model import GenericDraftGeneratorModel
from app.services.chat_service import ChatService
from app.schemas.detect_incident_dto import DetectIncidentDto
from app.schemas.detect_incident_response import DetectIncidentResponse
from app.schemas.generate_incident_draft_response import GenerateIncidentDraftResponse
from app.models.ollama_draft_generator_model import OllamaDraftGeneratorModel

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

service = ChatService(
    draftGeneratorModel=OllamaDraftGeneratorModel(
    model_name= settings.MODEL_NAME,
    base_url= settings.BASE_URL,
    api_key=settings.API_KEY,
)    if settings.MODEL_NAME == "qwen2.5:3b" else GenericDraftGeneratorModel(
    model_name= settings.MODEL_NAME,
    base_url= settings.BASE_URL,
    api_key=settings.API_KEY,
)
)
@router.post("/generate-incident-draft",
    response_model=GenerateIncidentDraftResponse,
        responses={
            500: {
                "description": "Model generation failed"
            },
        }    
    )
def generate_incident_draft(dto: DetectIncidentDto):
    return service.generate_incident_draft(dto.message)


@router.post("/detect-incident",
    response_model=DetectIncidentResponse         
    )
def detect_incident(dto: DetectIncidentDto):
    return service.detect_incident(dto.message)

