import os
from jinja2 import Environment, FileSystemLoader, select_autoescape


def create_file(path: str, content: str):
    """
    Create a file with the given path and content. Check if the file already exists.

    :param path: The path where the file will be created.
    :param content: The content to be written to the file.
    :return: None
    """
    if os.path.exists(path):
        print(f"Error: File already exists at {path}")
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as file:
        file.write(content)
    print(f"File created at: {path}")


def create_directory(path: str):
    """
    Create a directory at the given path.

    :param path: The path where the directory will be created.
    :return: None
    """
    os.makedirs(path, exist_ok=True)
    print(f"Directory created at: {path}")


def load_template(template_path: str, **kwargs) -> str:
    """
    Load a template file using Jinja2 and render it with the given keyword arguments.

    :param template_path: The path to the template file.
    :param kwargs: Data to replace placeholders in the template.
    :return: The populated template content as a string.
    """
    # Set up Jinja environment with the templates directory
    template_dir = os.path.dirname(template_path)
    template_name = os.path.basename(template_path)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        # Adjust autoescape as needed
        autoescape=select_autoescape(["html", "xml"]),
    )

    # Load and render the template
    template = env.get_template(template_name)
    return template.render(**kwargs)
