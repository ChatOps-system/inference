from pydantic import BaseModel

class DetectIncidentDto(BaseModel):
    message: str