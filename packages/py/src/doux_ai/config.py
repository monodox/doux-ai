import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    default_model: str = os.getenv("DOUX_DEFAULT_MODEL", "llama3.2:latest")
    ui_host: str = os.getenv("DOUX_UI_HOST", "127.0.0.1")
    ui_port: int = int(os.getenv("DOUX_UI_PORT", "7860"))
