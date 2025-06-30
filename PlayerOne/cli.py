import typer
from .engine import load_flow, run_interactive

app = typer.Typer()

@app.command()
def init(flow: str):
    """Initialize a new flow directory"""
    from pathlib import Path
    template_path = Path("PlayerOne/flow_templates/chatbot.yaml")
    target_path = Path(flow) / "flow.yaml"
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(template_path.read_text())
    print(f"Flow initialized at {target_path}")

@app.command()
def test(flow: str):
    """Run interactive flow"""
    flow_data = load_flow(flow)
    run_interactive(flow_data)

if __name__ == "__main__":
    app()
