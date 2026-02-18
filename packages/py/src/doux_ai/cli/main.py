import argparse
import sys
from dataclasses import replace

from doux_ai.config import Settings
from doux_ai.ollama import OllamaClient
from doux_ai.runtime import run_research
from doux_ai.ui import launch_ui


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="doux", description="Doux AI local research agent CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    doctor_cmd = sub.add_parser("doctor", help="Check local Ollama connectivity")
    doctor_cmd.add_argument("--base-url", default=None, help="Override Ollama base URL")

    run_cmd = sub.add_parser("run", help="Run a one-shot research query")
    run_cmd.add_argument("query", help="Prompt/query text")
    run_cmd.add_argument("--model", default=None, help="Model name (defaults to DOUX_DEFAULT_MODEL)")

    ui_cmd = sub.add_parser("ui", help="Launch Gradio UI")
    ui_cmd.add_argument("--host", default=None, help="Host binding")
    ui_cmd.add_argument("--port", type=int, default=None, help="Port binding")

    return parser


def _doctor(base_url: str | None) -> int:
    settings = Settings()
    client = OllamaClient(base_url=base_url or settings.ollama_base_url)
    status = client.health()
    if status.ok:
        print(f"OK: {status.message}")
        return 0
    print(f"ERROR: {status.message}")
    print("Fix: run `ollama serve` and verify OLLAMA_BASE_URL.")
    return 1


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    if args.command == "doctor":
        return _doctor(args.base_url)

    if args.command == "run":
        try:
            result = run_research(query=args.query, model=args.model)
            print(result.output)
            return 0
        except Exception as exc:
            print(f"Run failed: {exc}", file=sys.stderr)
            return 1

    if args.command == "ui":
        settings = Settings()
        settings = replace(
            settings,
            ui_host=args.host if args.host is not None else settings.ui_host,
            ui_port=args.port if args.port is not None else settings.ui_port,
        )
        launch_ui(settings=settings)
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
