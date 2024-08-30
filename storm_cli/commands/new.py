# storm_cli/commands/new.py

import typer

def new_project(name: str):
    """
    Scaffolds a new Storm project.
    """
    typer.echo(f"Creating a new Storm project: {name}")
