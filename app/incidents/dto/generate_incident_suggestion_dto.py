from pydantic import BaseModel, Field

class GenerateIncidentSuggestionDto(BaseModel):
    message: str = Field(..., description="The message to generate an incident suggestion", examples=["Se produjo una caída de energía repentina en la planta principal. Varias máquinas se apagaron de inmediato y los paneles de control mostraron alertas intermitentes. El equipo de mantenimiento no ha identificado la causa."])
    