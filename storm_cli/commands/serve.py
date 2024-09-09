import typer
import subprocess
import os
from storm_cli.utils.logger import setup_logger

app = typer.Typer()
logger = setup_logger("Serve")


@app.command()
def start(
    env: str = typer.Option(
        "development",
        help="The environment to run the application in (e.g., development, production).",
    ),
    port: int = typer.Option(8000, help="The port number to run the server on."),
    reload: bool = typer.Option(True, help="Enable auto-reload for development."),
    host: str = typer.Option("0.0.0.0", help="The host address to bind the server to."),
):
    """
    Serve the Storm application.

    :param env: The environment to run the application in.
    :param port: The port to run the application on.
    :param reload: Whether to enable auto-reload (useful in development).
    :param host: The host address to bind the server to.
    :return: None
    """
    logger.info(f"Starting Storm application in {env} mode on {host}:{port}.")

    # Load environment variables from a file (e.g., .env file specific to the environment)
    env_file = f".env.{env}"
    if os.path.exists(env_file):
        logger.info(f"Loading environment variables from {env_file}.")
        load_env_file(env_file)

    # Determine the server command based on the environment
    server_command = [
        "uvicorn",  # Replace with your specific server command if different
        "src.main:app",  # Replace with the entry point of your application
        "--host",
        host,
        "--port",
        str(port),
    ]

    if reload and env == "development":
        server_command.append("--reload")

    try:
        logger.info(f"Running server command: {' '.join(server_command)}")
        subprocess.run(server_command, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to start the application: {e}")
        raise typer.Exit(code=1)


def load_env_file(filepath: str):
    """
    Load environment variables from a specified file.

    :param filepath: Path to the environment file.
    :return: None
    """
    with open(filepath) as file:
        for line in file:
            if line.startswith("#") or not line.strip():
                continue
            key, value = line.strip().split("=", 1)
            os.environ[key] = value
            logger.info(f"Loaded {key} from {filepath}")


if __name__ == "__main__":
    app()
