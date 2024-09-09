import typer
import subprocess
import os
from storm_cli.utils.logger import setup_logger

app = typer.Typer()
logger = setup_logger("Build")


@app.command()
def build(
    env: str = typer.Option(
        "production",
        help="The environment to build for (e.g., production, staging, development).",
    ),
    clean: bool = typer.Option(False, help="Clean previous builds before building."),
    optimize: bool = typer.Option(True, help="Optimize the build output."),
    docker: bool = typer.Option(False, help="Build a Docker image for deployment."),
):
    """
    Build the Storm application for deployment.

    :param env: The environment to build for.
    :param clean: Whether to clean previous builds.
    :param optimize: Whether to optimize the build output.
    :param docker: Whether to build a Docker image.
    :return: None
    """
    logger.info(f"Building Storm application for {env} environment.")

    # Clean previous builds if specified
    if clean:
        logger.info("Cleaning previous builds...")
        clean_build()

    # Run pre-build tasks, such as compiling assets
    logger.info("Running pre-build tasks...")
    pre_build_tasks(env)

    # Run the build process (e.g., bundling, compiling)
    logger.info("Running build process...")
    try:
        build_application(env, optimize)
        logger.info("Build completed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Build process failed: {e}")
        raise typer.Exit(code=1)

    # Optionally build a Docker image
    if docker:
        logger.info("Building Docker image...")
        try:
            build_docker_image(env)
            logger.info("Docker image built successfully.")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to build Docker image: {e}")
            raise typer.Exit(code=1)


def clean_build():
    """
    Clean up previous build artifacts.

    :return: None
    """
    try:
        # Example: Remove build directories or files
        subprocess.run(["rm", "-rf", "build/", "dist/"], check=True)
        logger.info("Cleaned previous build artifacts.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error cleaning build artifacts: {e}")


def pre_build_tasks(env: str):
    """
    Run tasks required before the build, such as compiling assets or running migrations.

    :param env: The environment for the build.
    :return: None
    """
    try:
        # Example: Compile TypeScript, run asset-related tasks, or migrations
        if env == "production":
            subprocess.run(
                ["echo", "Running production-specific pre-build tasks..."], check=True
            )
        else:
            subprocess.run(["echo", "Running pre-build tasks for", env], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error in pre-build tasks: {e}")
        raise typer.Exit(code=1)


def build_application(env: str, optimize: bool):
    """
    Build the application by running the necessary bundling or compilation commands.

    :param env: The environment to build for.
    :param optimize: Whether to optimize the build output.
    :return: None
    """
    build_command = ["echo", f"Building application for {env} environment..."]

    if optimize:
        build_command.append("--optimize")

    try:
        subprocess.run(build_command, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error building the application: {e}")
        raise typer.Exit(code=1)


def build_docker_image(env: str):
    """
    Build a Docker image for the application.

    :param env: The environment for which the Docker image is being built.
    :return: None
    """
    try:
        docker_command = ["docker", "build", "-t", f"storm_app:{env}", "."]
        subprocess.run(docker_command, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error building Docker image: {e}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
