import typer
from storm_cli.commands import new, generate, build, start, info, add, lint, new, config

app = typer.Typer(
    help="Storm CLI - A command-line tool for managing Storm applications."
)

# Register typers
app.add_typer(
    new.app,
    name="new",
    help="Generate a new Storm application.",
)
app.add_typer(start.app, name="start", help="Run a Storm application.")
app.add_typer(info.app, help="Display Storm project details.")
app.add_typer(
    add.app, name="add", help="Add support for an external library to your project."
)
app.add_typer(generate.app, name="generate", help="Generate a Storm element.")
app.add_typer(config.app, name="config", help="Configure Storm CLI settings.")

# Register commands
app.command()(info.info)
app.command()(lint.lint)
app.command()(build.build)
app.command()(new.new)

# Version and Help options
@app.callback()
def main(
    version: bool = typer.Option(
        None, "--version", "-v", help="Output the current version."
    )
):
    if version:
        typer.echo("Storm CLI Version 0.1.0")
        raise typer.Exit()


if __name__ == "__main__":
    app()
