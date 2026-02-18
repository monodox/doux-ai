# Doux AI

Doux AI is a local-first, open-source research agent framework powered by Ollama.

Doux AI runs on your machine and gives you structured, reproducible research workflows through a typed Python and TypeScript toolchain.

## What Doux AI Is

- A self-hosted research agent runtime
- A local LLM orchestration engine
- An OSS framework for autonomous and collaborative research workflows
- A `pip` and `npm` distributed developer toolchain
- Ollama-native by default

## What Doux AI Is Not

- Just a chatbot
- Just a wrapper around Ollama
- Just a UI

## Core Capabilities

- Local runtime for model execution through Ollama
- Agent orchestration primitives for multi-step research tasks
- Retrieval and structured workflows for repeatable analysis
- Typed APIs for Python and TypeScript consumers
- CLI for automation and scripting
- Gradio web UI for local interactive use

## Quickstart

Prerequisites:

- Python 3.10+
- Node.js 20+ (optional, for TS tools)
- Ollama installed locally

Run locally:

```bash
ollama serve
ollama pull llama3.2:latest
pip install -e packages/py
doux doctor
doux run "Summarize local-first AI systems"
doux ui
```

The Gradio UI runs on `http://127.0.0.1:7860` by default.

## Configuration

Environment variables:

- `OLLAMA_BASE_URL` default: `http://localhost:11434`
- `DOUX_DEFAULT_MODEL` default: `llama3.2:latest`
- `DOUX_UI_HOST` default: `127.0.0.1`
- `DOUX_UI_PORT` default: `7860`

See `.env.example` for a starter template.

## CLI

Commands:

- `doux doctor` checks Ollama connectivity
- `doux run "<query>"` runs a one-shot research prompt
- `doux ui` launches the Gradio interface

## Docker

Optional Docker-based local run:

```bash
docker compose -f docker/docker-compose.yml up --build
```

Services include Ollama and Doux UI.

## Repository Layout

- `packages/py` Python runtime, CLI, Ollama client, Gradio integration
- `packages/ts/packages/cli` TypeScript companion CLI
- `docker` compose and Dockerfiles
- `website` GitHub Pages landing site

## Open Source

- License: MIT (`LICENSE`)
- Security policy: `SECURITY.md`
- Contributing guide: `CONTRIBUTING.md`
- Code of conduct: `CODE_OF_CONDUCT.md`
- Changelog: `CHANGELOG.md`
- Roadmap: `ROADMAP.md`

## Status

Current status: early scaffold with local runtime, CLI, and Gradio UI ready for iterative development.