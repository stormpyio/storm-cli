import typer
from storm_cli.utils.file_manager import create_file, load_template
from storm_cli.utils.logger import setup_logger
import os

app = typer.Typer(help="Generate various elements for Storm applications.")
logger = setup_logger("Generate")

# Available schematics with corresponding template directories and files
SCHEMATICS = {
    "module": "module_template.txt",
    "controller": "controller_template.txt",
    "service": "service_template.txt",
}


@app.command("module")
def module(name: str, path: str = "."):
    """
    Generate a new module.

    :param name: The name of the module.
    :param path: The path where the module will be generated.
    :return: None
    """
    generate("module", name, path)


@app.command("controller")
def generate_controller(name: str, path: str = "."):
    """
    Generate a new controller.

    :param name: The name of the controller.
    :param path: The path where the controller will be generated.
    :return: None
    """
    generate("controller", name, path)


@app.command("service")
def generate_service(name: str, path: str = "."):
    """
    Generate a new service.

    :param name: The name of the service.
    :param path: The path where the service will be generated.
    :return: None
    """
    generate("service", name, path)


def generate(schematic: str, name: str, path: str):
    """
    General function to generate elements using Jinja2 templates.

    :param schematic: The type of element to generate (e.g., module, controller, service).
    :param name: The name of the element.
    :param path: The path where the element will be generated.
    :return: None
    """
    if schematic not in SCHEMATICS:
        logger.error(
            f"Schematic '{schematic}' is not recognized. Available schematics: {list(SCHEMATICS.keys())}"
        )
        raise typer.Exit(code=1)

    template_file = SCHEMATICS[schematic]
    template_path = os.path.join("storm_cli", "templates", template_file)

    logger.info(
        f"Generating {schematic} named '{name}' using template '{template_file}'."
    )

    # Load and populate the template using Jinja
    try:
        content = load_template(template_path, name=name)
        output_filename = f"{name.lower()}.py"
        file_path = os.path.join(
            path, output_filename
        )  # Define the output path and file name
        create_file(file_path, content)
        logger.info(f"Generated {schematic} at {file_path}.")
    except Exception as e:
        typer.echo(f"Error generating {schematic}: {e}")
        logger.error(f"Error generating {schematic}: {e}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
