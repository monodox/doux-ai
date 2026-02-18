import gradio as gr

from doux_ai.config import Settings
from doux_ai.runtime import run_research


def _run(query: str, model: str) -> str:
    if not query.strip():
        return "Please enter a query."
    result = run_research(query=query, model=model.strip() or None)
    return result.output


def launch_ui(settings: Settings | None = None) -> None:
    resolved = settings or Settings()

    with gr.Blocks(title="Doux AI") as demo:
        gr.Markdown("# Doux AI\nLocal-first OSS research agent framework powered by Ollama.")
        query = gr.Textbox(label="Research query", lines=5, placeholder="Ask for synthesis, summary, or extraction")
        model = gr.Textbox(label="Model", value=resolved.default_model)
        run_button = gr.Button("Run")
        output = gr.Markdown(label="Result")
        run_button.click(_run, inputs=[query, model], outputs=[output])

    demo.launch(server_name=resolved.ui_host, server_port=resolved.ui_port)
