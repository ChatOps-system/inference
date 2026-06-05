from abc import ABC, abstractmethod
from app.schemas.incident_draft import IncidentDraft

class DraftGeneratorModel(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> IncidentDraft:
        pass