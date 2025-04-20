"""
CLI commands to generate components (controller, service, etc.) using Copier templates.
"""

import os
import questionary
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
    src_path = current_dir / "src"
    folders = [f for f in src_path.iterdir() if f.is_dir()]
    if not folders:
        print("[bold red]No folders found in src/. Please create one first.[/bold red]")
        raise typer.Exit(code=1)

    selected_folder = questionary.select(
        "Select the folder to place your controller in:",
        choices=[f.name for f in folders]
    ).ask()
    
    if not selected_folder:
        raise typer.Exit(code=1)

    template_path = Path(__file__).parent.parent.parent.parent / "templates" / "controller"
    output_path = src_path / selected_folder / "controllers" 

    context = {"package_name": name}

    print(f"[bold green]Generating controller:[/bold green] {name}")
    
    existing_files = set(p.relative_to(output_path) for p in output_path.rglob("*") if p.is_file())
    run_copy(str(template_path), str(output_path), data=context, quiet=True)
    new_files = set(p.relative_to(output_path) for p in output_path.rglob("*") if p.is_file()) - existing_files

    for file_path in sorted(new_files):
        size = os.path.getsize(output_path / file_path)
        relative_path = Path("src") / selected_folder / "controllers"
        print(f"[yellow]>[/yellow] CREATE {relative_path}/{file_path} ({size} bytes)")

    print(f"[bold cyan]✓ Controller created in {output_path}[/bold cyan]")

@app.command("service")
def generate_service(name: str):
    """
    Generates a new service from a Copier template.
    """
    current_dir = Path.cwd()
    src_path = current_dir / "src"
    folders = [f for f in src_path.iterdir() if f.is_dir()]
    if not folders:
        print("[bold red]No folders found in src/. Please create one first.[/bold red]")
        raise typer.Exit(code=1)

    selected_folder = questionary.select(
        "Select the folder to place your service in:",
        choices=[f.name for f in folders]
    ).ask()
    
    if not selected_folder:
        raise typer.Exit(code=1)

    template_path = Path(__file__).parent.parent.parent.parent / "templates" / "service"
    output_path = src_path / selected_folder / "services" 

    context = {"package_name": name}

    print(f"[bold green]Generating service:[/bold green] {name}")
    
    existing_files = set(p.relative_to(output_path) for p in output_path.rglob("*") if p.is_file())
    run_copy(str(template_path), str(output_path), data=context, quiet=True)
    new_files = set(p.relative_to(output_path) for p in output_path.rglob("*") if p.is_file()) - existing_files

    for file_path in sorted(new_files):
        size = os.path.getsize(output_path / file_path)
        relative_path = Path("src") / selected_folder / "services"
        print(f"[yellow]>[/yellow] CREATE {relative_path}/{file_path} ({size} bytes)")

    print(f"[bold cyan]✓ Service created in {output_path}[/bold cyan]")
