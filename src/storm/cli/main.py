"""
Main entry point for the Storm CLI.
"""

import typer
from storm.cli import init, generate

# Create a root CLI app
app = typer.Typer(help="⚡ Storm CLI — Scaffolding for your microservice projects")

# Add subcommands
app.add_typer(init.app, name="init", help="Initialize new projects or modules")
app.add_typer(generate.app, name="generate", help="Generate components like controllers or services")

if __name__ == "__main__":
    app()
