from pydantic import BaseModel
from app.schemas.incident_draft import IncidentDraft


class GenerateIncidentDraftResponse(BaseModel):
    incident_draft: IncidentDraft
    message: str
    model_config = {
        "json_schema_extra":{
            "example": {
                
                    "incident_draft": {
                        "title": "Incidente de apagón abrupto en planta principal",
                        "description": "El sistema eléctrico se vio afectado por una caída repentina de energía, lo cual provocó el apagón inmediato y alertas en los paneles de control.",
                        "severity": "Medium",
                        "category": "Operational",
                        "location": "Planta principal",
                        "immediateActions": "Implementar la seguridad de emergencia para garantizar que todos los equipos se desconecten, incluyendo máquinas en alta peligrosidad.",
                        "recommendations": "Despejar el lugar de accidente y realizar una inspección exhaustiva del sistema eléctrico para encontrar la causa. También buscar un representante de mantenimiento experto para ayudar a diagnosticar la situación y ofrecer soluciones."
                    },
                    "message": "incident draft generated successfully for message Se produjo una caída de energía repentina en la planta principal. Varias máquinas se apagaron de inmediato y los paneles de control mostraron alertas intermitentes. El equipo de mantenimiento no ha identificado la causa."
                
            }
        }
    }
 