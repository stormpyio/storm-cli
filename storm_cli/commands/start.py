import typer
import subprocess
from storm_cli.utils.logger import setup_logger

app = typer.Typer()
logger = setup_logger("StartCommand")


@app.command()
def start(app: str = typer.Argument(None, help="The application to run")):
    """
    Run a Storm application.

    :param app: The name of the application to run.
    :return: None
    """
    app_name = app if app else "current"
    logger.info(f"Starting the Storm application: {app_name}")

    try:
        # Example: Replace with actual start command
        subprocess.run(["echo", f"Starting {app_name}..."], check=True)
        logger.info(f"Successfully started {app_name}!")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error starting the application: {e}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
