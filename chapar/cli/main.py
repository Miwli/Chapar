"""Entry point for the Chapar CLI."""

import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def hello() -> None:
    """A temporary test command to verify the CLI works."""
    print("Chapar is alive!")


@app.command()
def version() -> None:
    """Show the current Chapar version."""
    from chapar import __version__

    print(f"Chapar v{__version__}")