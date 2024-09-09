import typer
import os
from storm_cli.utils.logger import setup_logger

app = typer.Typer()
logger = setup_logger("Console")


@app.command()
def open():
    """
    Open an interactive console (REPL) for the Storm application.

    This command launches a Python shell or IPython shell (if available)
    with the application context preloaded.
    """
    logger.info("Opening the Storm console...")

    # Attempt to open IPython if available, otherwise fall back to Python REPL
    try:
        from IPython import embed

        logger.info("Starting IPython shell...")
        embed(colors="neutral")
    except ImportError:
        logger.warning(
            "IPython is not installed. Falling back to the standard Python shell."
        )
        import code

        # Define any local context variables if needed
        local_context = {}
        code.interact(local=local_context)


if __name__ == "__main__":
    app()
