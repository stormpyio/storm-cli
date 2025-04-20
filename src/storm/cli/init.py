"""
CLI commands to initialize a new project using Copier templates.
"""

import os
import typer
from rich import print
from pathlib import Path
from copier import run_copy

app = typer.Typer()

@app.command("project")
def init_project(name: str):
    """
    Initializes a new Storm project using the Copier project template.
    """
    current_dir = Path.cwd()
    template_path = Path(__file__).parent.parent.parent.parent / "templates" / "project"
    output_path = current_dir / name

    context = {
        "project_name": name,
        "package_name": name.lower().replace("-", "_").replace(" ", "_"),
    }

    print(f"[bold green]Creating new project:[/bold green] {name}")
    run_copy(str(template_path), str(output_path), data=context, quiet=True)

    for dirpath, dirnames, filenames in os.walk(output_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            size = os.path.getsize(file_path)
            relative_path = os.path.relpath(file_path, output_path)
            print(f"[yellow]>[/yellow] CREATE {relative_path} ({size} bytes)")

    print(f"[bold cyan]✓ Project initialized in {output_path}[/bold cyan]")
