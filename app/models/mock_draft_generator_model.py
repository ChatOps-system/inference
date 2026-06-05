from .draft_generator_model import DraftGeneratorModel
from app.schemas.incident_draft import IncidentDraft

class MockDraftGeneratorModel(DraftGeneratorModel):
    def generate(self, prompt: str) -> IncidentDraft:
        return IncidentDraft(
            title="Incidente de apagón abrupto en planta principal",
            description="El sistema eléctrico se vio afectado por una caída repentina de energía, lo cual provocó el apagón inmediato y alertas en los paneles de control.",
            severity="Medium",
            category="Operational",
            location="Planta principal",
            immediateActions="Implementar la seguridad de emergencia para garantizar que todos los equipos se desconecten.",
            recommendations="Despejar el lugar y realizar inspección del sistema eléctrico."
        )