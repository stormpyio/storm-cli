import typer
from storm_cli.utils.file_manager import create_file, create_directory
from storm_cli.utils.logger import setup_logger

app = typer.Typer()
logger = setup_logger("NewCommand")

@app.command()
def new(app_name: str):
    """
    Create a new Storm application.

    :param app_name: The name of the new Storm application.
    :return: None
    """
    logger.info(f"Creating a new Storm application: {app_name}")

    # Define the structure of the new Storm application
    directories = [
        f"{app_name}/src",
        f"{app_name}/src/controllers",
        f"{app_name}/src/services",
        f"{app_name}/src/modules",
        f"{app_name}/tests",
    ]

    files = {
        f"{app_name}/src/main.py": "# Entry point for the Storm application\n\nif __name__ == '__main__':\n    print('Hello, Storm!')",
        f"{app_name}/src/controllers/__init__.py": "# Controllers module\n",
        f"{app_name}/src/services/__init__.py": "# Services module\n",
        f"{app_name}/src/modules/__init__.py": "# Modules module\n",
        f"{app_name}/tests/test_basic.py": "# Basic test case\n\ndef test_basic():\n    assert True",
        f"{app_name}/requirements.txt": "typer\n",
        f"{app_name}/.gitignore": "*.pyc\n__pycache__/\n.env\n",
        f"{app_name}/README.md": f"# {app_name.capitalize()}\n\nThis is a new Storm application.\n",
    }

    # Create directories
    for directory in directories:
        create_directory(directory)
        logger.info(f"Created directory: {directory}")

    # Create files with initial content
    for filepath, content in files.items():
        create_file(filepath, content)
        logger.info(f"Created file: {filepath}")

    logger.info(f"Successfully created Storm application '{app_name}'.")

if __name__ == "__main__":
    app()
