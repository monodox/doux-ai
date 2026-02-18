# Contributing

Thanks for contributing to Doux AI.

## Development Setup

1. Start Ollama locally.
2. Install Python package in editable mode.
3. Run CLI checks.

```bash
ollama serve
ollama pull llama3.2:latest
pip install -e packages/py
doux doctor
```

## Project Areas

- Python runtime and CLI: `packages/py`
- TypeScript tools: `packages/ts/packages/cli`
- Docker setup: `docker`
- Website landing page: `website`

## Contribution Workflow

1. Create a feature branch.
2. Keep changes scoped and testable.
3. Update docs when behavior changes.
4. Add an entry to `CHANGELOG.md` for user-visible changes.
5. Open a pull request with clear rationale and verification steps.

## Pull Request Checklist

- Code builds locally
- New behavior is documented
- Breaking changes are explicitly called out
- No secrets or credentials are committed

## Commit Style

Recommended conventional prefixes:

- `feat:` new functionality
- `fix:` bug fix
- `docs:` documentation only
- `refactor:` internal restructuring
- `chore:` maintenance