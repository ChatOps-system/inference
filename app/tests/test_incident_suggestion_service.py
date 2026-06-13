from app.incidents.services.incident_suggestion_service import IncidentSuggestionService

def test_generate_incident_suggestion():
    service = IncidentSuggestionService()
    message = "Se produjo una caída de energía repentina en la planta principal. Varias máquinas se apagaron de inmediato y los paneles de control mostraron alertas intermitentes. El equipo de mantenimiento no ha identificado la causa."
    result = service.generate_incident_suggestion(message)
    assert result.incidentSuggestion is not None
    assert result.message is not None

    assert isinstance(result.incidentSuggestion.title, str)
    assert isinstance(result.incidentSuggestion.description, str)
    assert isinstance(result.incidentSuggestion.location, str)
    assert isinstance(result.incidentSuggestion.immediateActions, str)
    assert isinstance(result.incidentSuggestion.recommendations, str)
    assert result.incidentSuggestion.severity in ["High", "Medium", "Low"]
    assert result.incidentSuggestion.category in ["Safety", "Operational", "Equipment"]