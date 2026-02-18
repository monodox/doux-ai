from dataclasses import dataclass

from doux_ai.config import Settings
from doux_ai.ollama import OllamaClient


@dataclass
class ResearchResult:
    model: str
    output: str


def run_research(query: str, model: str | None = None, settings: Settings | None = None) -> ResearchResult:
    resolved = settings or Settings()
    resolved_model = model or resolved.default_model
    client = OllamaClient(base_url=resolved.ollama_base_url)
    output = client.generate(model=resolved_model, prompt=query)
    return ResearchResult(model=resolved_model, output=output)
