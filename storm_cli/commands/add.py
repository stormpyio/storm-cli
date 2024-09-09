import typer
from storm_cli.utils.logger import setup_logger

app = typer.Typer()
logger = setup_logger("AddCommand")

@app.command()
def lib(library: str):
    """
    Add support for an external library to your project.

    :param library: The library to add.
    :return: None
    """
    logger.info(f"Adding library {library} to the project...")
    # Example: Implement logic to add the specified library
    typer.echo(f"Library {library} added successfully.")

if __name__ == "__main__":
    app()
