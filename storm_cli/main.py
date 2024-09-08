import typer
from storm_cli.commands import new
from storm_cli.commands import generate

app = typer.Typer(help="Storm CLI - A command-line tool for managing Storm applications.")

# Register commands
app.add_typer(generate.app, name="generate")

if __name__ == "__main__":
    app()
