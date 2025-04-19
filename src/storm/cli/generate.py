"""
CLI commands to generate components (controller, service, etc.) using Copier templates.
"""

import typer
from rich import print
from pathlib import Path
from copier import run_copy

app = typer.Typer()

@app.command("controller")
def generate_controller(name: str):
    """
    Generates a new controller from a Copier template.
    """
    current_dir = Path.cwd()
    template_path = Path(__file__).parent.parent.parent / "templates" / "controller"
    output_path = current_dir / "src" / "controllers" / name.lower()

    context = {"name": name}

    print(f"[bold green]Generating controller:[/bold green] {name}")
    run_copy(str(template_path), str(output_path), data=context, quiet=True)
    print(f"[bold cyan]✓ Controller created in {output_path}[/bold cyan]")
