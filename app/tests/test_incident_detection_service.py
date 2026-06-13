from app.incidents.services.incident_detection_service import IncidentDetectionService

def test_detect_incident():
    service = IncidentDetectionService()
    message = "Se produjo una caída de energía repentina en la planta principal. Varias máquinas se apagaron de inmediato y los paneles de control mostraron alertas intermitentes. El equipo de mantenimiento no ha identificado la causa."
    result = service.detect_incident(message)
    assert isinstance(result.isIncident, bool)
    assert isinstance(result.confidence, float)
    assert isinstance(result.message, str)