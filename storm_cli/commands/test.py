import typer
import subprocess
from storm_cli.utils.logger import setup_logger

app = typer.Typer()
logger = setup_logger("Test")

@app.command()
def test(
    path: str = typer.Argument(None, help="Path to the test file or directory to run (default: all tests)."),
    coverage: bool = typer.Option(False, help="Run tests with coverage report."),
    verbose: bool = typer.Option(False, help="Run tests in verbose mode."),
    failed: bool = typer.Option(False, help="Run only the tests that failed last time."),
):
    """
    Run tests for the Storm application.

    :param path: The path to the test file or directory to run.
    :param coverage: Whether to run tests with a coverage report.
    :param verbose: Whether to run tests in verbose mode.
    :param failed: Whether to run only the tests that failed last time.
    :return: None
    """
    # Default command for running tests
    test_command = ["pytest"]

    # Add path if specified
    if path:
        test_command.append(path)

    # Add options for coverage, verbosity, and rerunning failed tests
    if coverage:
        test_command = ["pytest", "--cov", path or "."]  # Ensure coverage applies to the correct path
    if verbose:
        test_command.append("-v")
    if failed:
        test_command = ["pytest", "--last-failed"]

    # Execute the test command
    try:
        logger.info(f"Running tests with command: {' '.join(test_command)}")
        subprocess.run(test_command, check=True)
        logger.info("Tests completed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Test run failed: {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
