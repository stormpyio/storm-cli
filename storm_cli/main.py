# storm_cli/main.py

import typer
from storm_cli.commands import new

app = typer.Typer(help="Storm CLI - A command-line tool for managing Storm applications.")

# Register commands
app.command()(new.new_project)


if __name__ == "__main__":
    app()
