import typer
from storm_cli.utils.logger import setup_logger

app = typer.Typer()
logger = setup_logger("InfoCommand")


@app.command()
def info():
    """
    Display Storm project details.

    :return: None
    """
    logger.info("Displaying Storm project details...")
    # Example: Add logic to retrieve and display project details
    typer.echo("Project Name: Example Storm Project")
    typer.echo("Version: 1.0.0")
    typer.echo("Description: This is an example Storm project.")
