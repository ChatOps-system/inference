from app.models.mock_draft_generator_model import MockDraftGeneratorModel
from app.services.chat_service import ChatService

def test_detect_incident():
    service = ChatService(draftGeneratorModel=MockDraftGeneratorModel())
    message = "Se produjo una caída de energía repentina en la planta principal. Varias máquinas se apagaron de inmediato y los paneles de control mostraron alertas intermitentes. El equipo de mantenimiento no ha identificado la causa."
    result = service.detect_incident(message)
    assert result.isIncident is True
    assert result.confidence > 0
    assert isinstance(result.message, str)

def test_generate_incident_draft():
    service = ChatService(draftGeneratorModel=MockDraftGeneratorModel())

    message = "Se produjo una caída de energía repentina en la planta principal. Varias máquinas se apagaron de inmediato y los paneles de control mostraron alertas intermitentes. El equipo de mantenimiento no ha identificado la causa."
    result = service.generate_incident_draft(message)

    assert result.incident_draft is not None
    assert result.message is not None

    assert isinstance(result.incident_draft.title, str)
    assert isinstance(result.incident_draft.description, str)
    assert isinstance(result.incident_draft.location, str)
    assert isinstance(result.incident_draft.immediateActions, str)
    assert isinstance(result.incident_draft.recommendations, str)
    assert result.incident_draft.severity in ["High", "Medium", "Low"]
    assert result.incident_draft.category in ["Safety", "Operational", "Equipment"]