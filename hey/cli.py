from datetime import datetime
from typing import Annotated, Optional

import typer
import keyring
import getpass
from rich.markdown import Markdown
from rich.panel import Panel

from hey import __version__, console
from hey.configs import cli, configs
from hey.consts import APP_NAME
from hey.editor import open_tmp_editor
from hey.openai import answer

app = typer.Typer()
app.add_typer(cli.app, name="config")


def version_callback(value: bool):
    if value:
        print(f"Hey - {__version__}!")
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    no_style: Annotated[
        bool, typer.Option("--no-style", "--ns", help="Don't style the output.")
    ] = configs.get("never_style"),
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-V",
            callback=version_callback,
            help=f"Show the current version of {APP_NAME}.",
        ),
    ] = None,
):
    """
    Hey is a pair-programming friend that interacts with ChatGPT and responds back in a pretty style. ✨
    """

    if ctx.invoked_subcommand is None:
        user_input = open_tmp_editor()
        markdown_input = Markdown(
            user_input, code_theme=configs.get("code_block_theme")
        )

        user_panel = Panel(
            markdown_input,
            title=":bust_in_silhouette:",
            title_align="left",
            subtitle=datetime.now().strftime("%H:%M"),
            subtitle_align="right",
            style="blue",
        )

        console.print(user_panel)
        result = answer(user_input, no_style)
        console.print(result)


@app.command()
def ask(
    user_input: str,
    no_style: Annotated[
        bool, typer.Option("--no-style", "--ns", help="Don't style the output.")
    ] = configs.get("never_style"),
):
    """
    Ask Hey directly in-command.
    """

    result = answer(user_input, no_style)
    console.print(result)

@app.command()
def auth():
    """
    Take HEY_TOKEN from user.
    """
    password = getpass.getpass("Copy and paste your token here, [Token will not be echoed] > ")
    keyring.set_password("system","HEY_TOKEN",password)
