import os

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
