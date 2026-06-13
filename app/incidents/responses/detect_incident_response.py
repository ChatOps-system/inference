from pydantic import BaseModel


class DetectIncidentResponse(BaseModel):
    isIncident: bool
    confidence: float
    message: str
    model_config = {
    "json_schema_extra":{
        "example": {
            "isIncident": True,
            "confidence": 0.8,
            "message": "Detected incident for message: Se produjo una caída de energía repentina en la planta principal. Varias máquinas se apagaron de inmediato y los paneles de control mostraron alertas intermitentes. El equipo de mantenimiento no ha identificado la causa."            
        }
    }
}
