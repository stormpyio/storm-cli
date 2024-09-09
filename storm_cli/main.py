import typer
from storm_cli.commands import new, generate, build, test

app = typer.Typer(help="Storm CLI - A command-line tool for managing Storm applications.")

# Register commands
app.add_typer(generate.app, name="generate")
app.add_typer(build.app, name="build")
app.add_typer(test.app, name="test")
app.add_typer(new.app, name="new")


if __name__ == "__main__":
    app()
