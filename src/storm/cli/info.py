import typer
from rich import print

app = typer.Typer(invoke_without_command=True)

ascii_art = r"""
███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗     ██████╗██╗     ██╗
██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║    ██╔════╝██║     ██║
███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║    ██║     ██║     ██║
╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║    ██║     ██║     ██║
███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║    ╚██████╗███████╗██║
╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝╚══════╝╚═╝
"""

def get_version(package: str) -> str:
    try:
        import importlib.metadata
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return "Not installed"

@app.callback()
def info():
    """
    Displays system and Storm CLI environment information.
    """
    import platform
    import importlib.metadata


    print(f"[bold magenta]{ascii_art}[/bold magenta]")

    print("[bold yellow][System Information][/bold yellow]")
    print(f"OS Version         : {platform.system()} {platform.release()}")
    print(f"Python Version     : {platform.python_version()}")
    
    print("\n[bold yellow][Storm CLI][/bold yellow]")
    print(f"Storm CLI Version  : {get_version('storm')}")

    print("\n[bold yellow][Storm CLI Dependencies][/bold yellow]")
    pkgs = ["typer", "copier", "rich"]
    for pkg in pkgs:
        try:
            version = importlib.metadata.version(pkg)
        except importlib.metadata.PackageNotFoundError:
            version = "Not installed"
        print(f"{pkg} version : {version}")
