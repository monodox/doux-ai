from dataclasses import dataclass
from typing import Any

import httpx


@dataclass
class OllamaStatus:
    ok: bool
    message: str


class OllamaClient:
    def __init__(self, base_url: str, timeout_seconds: float = 60.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds

    def health(self) -> OllamaStatus:
        try:
            response = httpx.get(f"{self.base_url}/api/tags", timeout=self.timeout_seconds)
            response.raise_for_status()
            payload = response.json()
            models = payload.get("models", [])
            return OllamaStatus(ok=True, message=f"Connected. {len(models)} model(s) available.")
        except Exception as exc:
            return OllamaStatus(ok=False, message=f"Unable to reach Ollama at {self.base_url}: {exc}")

    def generate(self, model: str, prompt: str) -> str:
        # Prefer native Ollama endpoint, then fall back to chat-style endpoints.
        attempt_specs = [
            (
                "/api/generate",
                {"model": model, "prompt": prompt, "stream": False},
                "response",
            ),
            (
                "/api/chat",
                {"model": model, "messages": [{"role": "user", "content": prompt}], "stream": False},
                "message.content",
            ),
            (
                "/v1/chat/completions",
                {"model": model, "messages": [{"role": "user", "content": prompt}]},
                "choices.0.message.content",
            ),
        ]

        last_error: Exception | None = None
        for path, body, value_path in attempt_specs:
            try:
                response = httpx.post(f"{self.base_url}{path}", json=body, timeout=self.timeout_seconds)
                if response.status_code == 404:
                    error_text = ""
                    try:
                        error_payload = response.json()
                        error_text = str(error_payload)
                    except Exception:
                        error_text = response.text
                    if "model" in error_text.lower() and "not found" in error_text.lower():
                        raise RuntimeError(f"Model '{model}' not found in Ollama. Pull it with: ollama pull {model}")
                    continue
                response.raise_for_status()
                payload: dict[str, Any] = response.json()
                return self._read_value(payload, value_path).strip()
            except Exception as exc:
                last_error = exc

        if last_error is not None:
            raise last_error
        raise RuntimeError(f"No compatible generation endpoint found at {self.base_url}")

    def _read_value(self, payload: dict[str, Any], path: str) -> str:
        current: Any = payload
        for part in path.split("."):
            if part.isdigit():
                current = current[int(part)]
            else:
                current = current.get(part, "") if isinstance(current, dict) else ""
        return str(current or "")
