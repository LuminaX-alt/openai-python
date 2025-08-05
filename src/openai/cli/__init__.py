from ._cli import main as main
# openai/cli/main.py
import click

@click.group()
def cli():
    """OpenAI CLI — interact with the API from your terminal."""
    pass

@cli.command()
@click.option("--shell", type=click.Choice(["bash", "zsh", "fish", "powershell"]), help="Shell type.")
def install_completion(shell):
    """
    Install auto-completion for the OpenAI CLI.
    """
    click.echo(f"To enable completion for {shell}, run:")
    if shell == "bash":
        click.echo('eval "$(_OPENAI_COMPLETE=bash_source openai)"')
    elif shell == "zsh":
        click.echo('eval "$(_OPENAI_COMPLETE=zsh_source openai)"')
    elif shell == "fish":
        click.echo('eval (env _OPENAI_COMPLETE=fish_source openai)')
    elif shell == "powershell":
        click.echo('Invoke-Expression -Command $(_OPENAI_COMPLETE=powershell_source openai)')
    else:
        click.echo("Unsupported shell. Use one of: bash, zsh, fish, powershell.")
