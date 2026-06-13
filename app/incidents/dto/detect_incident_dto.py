from pydantic import BaseModel, Field

class DetectIncidentDto(BaseModel):
    message: str = Field(..., description="The message to detect an incident from", examples=["Se produjo una caída de energía repentina en la planta principal. Varias máquinas se apagaron de inmediato y los paneles de control mostraron alertas intermitentes. El equipo de mantenimiento no ha identificado la causa."])
    