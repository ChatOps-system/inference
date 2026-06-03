from fastapi import APIRouter
from app.schemas.chat import DetectIncidentDto
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

service = ChatService()

@router.post("/detect-incident")
def detect_incident(dto: DetectIncidentDto):
    return service.detect_incident(dto.message)

@router.post("/generate-incident-draft")
def generate_incident_draft(dto: DetectIncidentDto):
    return service.generate_incident_draft(dto.message)