import typer

app = typer.Typer()

config_store = {}  # Placeholder for configuration storage

@app.command()
def set(key: str, value: str):
    """
    Set a configuration value.

    :param key: The configuration key.
    :param value: The value to set for the configuration key.
    :return: None
    """
    config_store[key] = value
    typer.echo(f"Configuration set: {key} = {value}")

@app.command()
def get(key: str):
    """
    Get a configuration value.

    :param key: The configuration key.
    :return: None
    """
    value = config_store.get(key, "Not set")
    typer.echo(f"Configuration: {key} = {value}")

if __name__ == "__main__":
    app()
