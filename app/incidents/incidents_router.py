from fastapi import APIRouter
from app.incidents.dto.detect_incident_dto import DetectIncidentDto
from app.incidents.dto.generate_incident_suggestion_dto import GenerateIncidentSuggestionDto
from app.incidents.responses.detect_incident_response import DetectIncidentResponse
from app.incidents.responses.generate_incident_suggestion_response import GenerateIncidentSuggestionResponse
from app.incidents.services.incident_detection_service import IncidentDetectionService
from app.incidents.services.incident_suggestion_service import IncidentSuggestionService

class IncidentsRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/incidents", tags=["Incidents"])
        self.incident_suggestion_service = IncidentSuggestionService()
        self.incident_detection_service = IncidentDetectionService()

        self.router.post("/generate-incident-suggestion",
            response_model=GenerateIncidentSuggestionResponse,
            responses={
                422: {
                    "description": "Model can not generate a valid output",
                    "content": {
                        "application/json": {
                            "example": {                                
                                "detail": {
                                    "error": "Model validation failed after retries",
                                    "details": "<failed_attempts>\n\n<generation number=\"1\">\n<exception>\n    6 validation errors for IncidentSuggestion\ndescription\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\nseverity\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\ncategory\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\nlocation\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\nimmediateActions\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\nrecommendations\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\n</exception>\n<completion>\n    ChatCompletion(id='chatcmpl-614', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='{\\n  \"properties\": {\\n    \"title\": null,\\n    \"description\": null,\\n    \"severity\": null,\\n    \"category\": null,\\n    \"location\": null,\\n    \"immediateActions\": null,\\n    \"recommendations\": null\\n  },\\n  \"required\": [\\n    \"title\",\\n    \"description\",\\n    \"severity\",\\n    \"category\",\\n    \"location\",\\n    \"immediateActions\",\\n    \"recommendations\"\\n  ],\\n  \"title\": \"IncidentSuggestion\",\\n  \"type\": \"object\"\\n}', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None))], created=1781360734, model='qwen2.5:3b', object='chat.completion', moderation=None, service_tier=None, system_fingerprint='fp_ollama', usage=CompletionUsage(completion_tokens=110, prompt_tokens=621, total_tokens=731, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))\n</completion>\n</generation>\n\n</failed_attempts>\n\n<last_exception>\n    6 validation errors for IncidentSuggestion\ndescription\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\nseverity\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\ncategory\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\nlocation\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\nimmediateActions\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\nrecommendations\n  Field required [type=missing, input_value={'properties': {'title': ...tion', 'type': 'object'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\n</last_exception>"
                                }
                            }
                        }
                    }
                },
                503: {
                    "description": "Generate incident suggestion failed"
                }
            }
        )(self.generate_incident_suggestion)

        self.router.post("/detect-incident",
            response_model=DetectIncidentResponse
        )(self.detect_incident)

    def generate_incident_suggestion(self, dto: GenerateIncidentSuggestionDto):
        return self.incident_suggestion_service.generate_incident_suggestion(dto.message)

    def detect_incident(self, dto: DetectIncidentDto):
        return self.incident_detection_service.detect_incident(dto.message)