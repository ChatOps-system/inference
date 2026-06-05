from pydantic import BaseModel, Field
from typing import Literal


class IncidentDraft(BaseModel):
    title: str = Field(..., description="Short incident title")
    description: str = Field(..., description="Detailed incident description")
    severity: Literal["High", "Medium", "Low"] = Field(
        ..., description="Severity level of the incident"
    )
    category: Literal["Safety", "Operational", "Equipment"] = Field(
        ..., description="Incident category"
    )
    location: str = Field(..., description="Where the incident occurred")
    immediateActions: str = Field(
        ..., description="Immediate actions to mitigate the incident"
    )
    recommendations: str = Field(
        ..., description="Preventive recommendations"
    )