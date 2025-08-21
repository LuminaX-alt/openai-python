# cli/main.py
import typer

app = typer.Typer(help="Example CLI with shell completion support")

@app.command()
def hello(name: str):
    """Say hello to NAME."""
    typer.echo(f"Hello {name}!")

if __name__ == "__main__":
    app()

from __future__ import annotations

from argparse import ArgumentParser

from . import chat, audio, files, image, models, completions, fine_tuning


def register_commands(parser: ArgumentParser) -> None:
    subparsers = parser.add_subparsers(help="All API subcommands")

    chat.register(subparsers)
    image.register(subparsers)
    audio.register(subparsers)
    files.register(subparsers)
    models.register(subparsers)
    completions.register(subparsers)
    fine_tuning.register(subparsers)
eval "$(your-cli-tool --install-completion bash)"
eval "$(_YOUR_CLI_TOOL_COMPLETE=source_bash your-cli-tool)"
eval "$(your-cli-tool --install-completion zsh)"
autoload -U compinit
compinit
eval "$(_YOUR_CLI_TOOL_COMPLETE=source_zsh your-cli-tool)"
your-cli-tool --install-completion fish | source
your-cli-tool --install-completion fish > ~/.config/fish/completions/your-cli-tool.fish
your-cli-tool --install-completion powershell | Out-String | Invoke-Expression

