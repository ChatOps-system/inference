import instructor
from openai import OpenAI
from app.ai.schemas.incident_suggestion_schema import IncidentSuggestion
from app.config import settings

class InstructorService:
    def __init__(self):
        self.model_name=settings.MODEL_NAME
        self.base_url = settings.BASE_URL
        self.api_key = settings.API_KEY
        self.client = instructor.from_openai(
        OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
            
        ),
        mode=instructor.Mode.JSON
    )
        
    def generate_incident_suggestion(self, prompt: str) -> IncidentSuggestion:
        response = self.client.chat.completions.create(
            response_model=IncidentSuggestion,
            model = self.model_name,
            max_retries=1,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an industrial safety assistant.\n"
                        "Generate ONLY ONE IncidentSuggestion JSON object.\n"
                        "Return ONLY valid JSON.\n"
                        "Return a REAL object with values.\n"
                        "Do NOT return a schema.\n"
                        "Do NOT return properties.\n"
                        "Do NOT return type definitions.\n"
                        "Do NOT describe fields.\n"
                        "Do NOT return markdown.\n"
                        "Do NOT wrap response in ```json.\n"
                        "Do NOT return explanations.\n"
                        "Do NOT return a list.\n"
                        "Do NOT return multiple objects.\n"
                        "Do NOT omit any required field.\n"
                        "Use realistic industrial incident values.\n"
                        "Always respond in Spanish except enum values.\n"
                        "Severity must be one of: High, Medium, Low.\n"
                        "Category must be one of: Safety, Operational, Equipment.\n"
                        "\n"
                        "Example response:\n"
                        "{\n"
                        '  "title": "Derrame de aceite cerca de maquinaria",\n'
                        '  "description": "Se detectó un derrame de aceite hidráulico cerca de una máquina industrial durante el turno de mantenimiento.",\n'
                        '  "severity": "High",\n'
                        '  "category": "Safety",\n'
                        '  "location": "Área de mantenimiento industrial",\n'
                        '  "immediateActions": "Aislar la zona afectada y limpiar el derrame utilizando material absorbente.",\n'
                        '  "recommendations": "Implementar inspecciones periódicas y reforzar protocolos de mantenimiento preventivo."\n'
                        "}\n"
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response

        