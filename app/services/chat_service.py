class ChatService:

    def detect_incident(self, message: str):
        return {
            "incidentDetected": True,
            "message": f"Incident detected with description: {message}"
        }

    def generate_incident_draft(self, message: str):
        return {
            "title": "Machine 12 is overheating",
            "description": f"Based on: {message}",
            "severity": "High",
            "category": "Equipment",
            "location": "Factory Floor - Section A",
            "immediateActions": "Stop machine",
            "recommendations": "Inspect system"
        }