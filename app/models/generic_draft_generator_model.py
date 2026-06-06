import instructor
from openai import OpenAI
from .draft_generator_model import DraftGeneratorModel
from app.schemas.incident_draft import IncidentDraft

class GenericDraftGeneratorModel(DraftGeneratorModel):
    def __init__(
            self, 
            base_url: str, 
            api_key: str, 
            model_name: str
            ):
        self.base_url = base_url
        self.api_key = api_key
        self.model_name = model_name
        self.client = instructor.from_openai(
            OpenAI(
                base_url=self.base_url,
                api_key=self.api_key
            ),
            mode=instructor.Mode.TOOLS
        )

    def generate(self, prompt: str) -> IncidentDraft:
        response = self.client.chat.completions.create(
            model=self.model_name,
            response_model=IncidentDraft,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an industrial safety assistant.\n"
                        "Return ONLY ONE IncidentDraft.\n"
                        "Do NOT return a list.\n"
                        "Do NOT return multiple objects.\n"
                        "Do NOT omit any field.\n"
                        "Do NOT return partial objects.\n"
                        "Always respond in Spanish except enum values."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response
