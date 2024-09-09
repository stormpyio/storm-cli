import typer
import subprocess
import os
from storm_cli.utils.logger import setup_logger

app = typer.Typer()
logger = setup_logger("Deploy")

@app.command()
def deploy(
    env: str = typer.Option("production", help="The environment to deploy to (e.g., production, staging)."),
    docker: bool = typer.Option(False, help="Build and deploy using Docker."),
    remote: str = typer.Option("", help="Remote server or cloud provider for deployment (e.g., AWS, GCP, Azure)."),
    build: bool = typer.Option(True, help="Build the application before deploying."),
):
    """
    Deploy the Storm application.

    :param env: The environment to deploy to.
    :param docker: Whether to use Docker for deployment.
    :param remote: The remote server or cloud provider for deployment.
    :param build: Whether to build the application before deploying.
    :return: None
    """
    logger.info(f"Deploying Storm application to {env} environment.")

    # Step 1: Build the application if specified
    if build:
        logger.info("Building the application before deployment...")
        try:
            subprocess.run(["storm", "build", "--env", env], check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Build failed: {e}")
            raise typer.Exit(code=1)

    # Step 2: Deploy using Docker if specified
    if docker:
        logger.info("Deploying using Docker...")
        try:
            build_docker_image(env)
            push_docker_image(env)
        except subprocess.CalledProcessError as e:
            logger.error(f"Docker deployment failed: {e}")
            raise typer.Exit(code=1)

    # Step 3: Deploy to remote server or cloud provider
    if remote:
        logger.info(f"Deploying to remote server: {remote}...")
        try:
            deploy_to_remote(env, remote)
        except subprocess.CalledProcessError as e:
            logger.error(f"Remote deployment failed: {e}")
            raise typer.Exit(code=1)

    logger.info(f"Successfully deployed Storm application to {env} environment.")

def build_docker_image(env: str):
    """
    Build a Docker image for the application.

    :param env: The environment for which the Docker image is being built.
    :return: None
    """
    try:
        docker_command = [
            "docker", "build", "-t", f"storm_app:{env}", "."
        ]
        logger.info(f"Running command: {' '.join(docker_command)}")
        subprocess.run(docker_command, check=True)
        logger.info("Docker image built successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error building Docker image: {e}")
        raise typer.Exit(code=1)

def push_docker_image(env: str):
    """
    Push a Docker image to a remote repository.

    :param env: The environment for which the Docker image is being pushed.
    :return: None
    """
    try:
        docker_push_command = [
            "docker", "push", f"storm_app:{env}"
        ]
        logger.info(f"Running command: {' '.join(docker_push_command)}")
        subprocess.run(docker_push_command, check=True)
        logger.info("Docker image pushed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error pushing Docker image: {e}")
        raise typer.Exit(code=1)

def deploy_to_remote(env: str, remote: str):
    """
    Deploy the application to a remote server or cloud provider.

    :param env: The environment to deploy to.
    :param remote: The remote server or cloud provider.
    :return: None
    """
    try:
        ssh_command = [
            "ssh", remote, f"docker pull storm_app:{env} && docker run -d storm_app:{env}"
        ]
        logger.info(f"Running command: {' '.join(ssh_command)}")
        subprocess.run(ssh_command, check=True)
        logger.info(f"Application deployed to {remote} successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error deploying to remote server: {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
