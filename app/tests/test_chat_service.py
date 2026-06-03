from app.services.chat_service import ChatService

def test_detect_incident():
    service = ChatService()
    message = "Machine overheating"
    result = service.detect_incident(message)
    assert result == {
        "incidentDetected": True,
        "message": f"Incident detected with description: {message}"
    }
    
def test_generate_incident_draft():
    service = ChatService()
    message = "Machine 12 is overheating"
    result = service.generate_incident_draft(message)
    assert result["title"] == "Machine 12 is overheating"
    assert result["severity"] == "High"
    assert result["category"] == "Equipment"
    assert result["location"] == "Factory Floor - Section A"
    assert "Based on:" in result["description"]