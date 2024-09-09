import typer
import subprocess
from storm_cli.utils.logger import setup_logger

app = typer.Typer()
logger = setup_logger("Lint")


def run_command(command):
    """
    Helper function to run a subprocess command and handle errors.

    :param command: The command to run as a list of strings.
    :return: None
    """
    try:
        logger.info(f"Running command: {' '.join(command)}")
        subprocess.run(command, check=True)
        logger.info("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {e}")
        raise typer.Exit(code=1)


@app.command()
def lint(
    fix: bool = typer.Option(
        False, help="Automatically fix linting errors (uses Black)."
    ),
    check: bool = typer.Option(False, help="Check code style without making changes."),
    path: str = typer.Argument(
        ".", help="The path to the codebase to lint (default is current directory)."
    ),
):
    """
    Lint the codebase to ensure code quality.

    :param fix: Whether to automatically fix linting errors.
    :param check: Whether to just check the code style without making changes.
    :param path: The path to the codebase to lint.
    :return: None
    """
    if fix:
        logger.info("Linting and fixing errors using Black...")
        fix_command = ["black", path]
        run_command(fix_command)

    if check:
        logger.info("Checking code style using Flake8...")
        check_command = ["flake8", path]
        run_command(check_command)

    if not fix and not check:
        logger.info("Running both lint check and fix...")
        fix_command = ["black", path]
        check_command = ["flake8", path]
        run_command(fix_command)
        run_command(check_command)


if __name__ == "__main__":
    app()
