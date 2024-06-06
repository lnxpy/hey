import os
import subprocess

import typer
from rich.prompt import Confirm

from hey import console
from hey.configs.utils import app_dir_exists, config_exists, init_config
from hey.consts import APP_CONFIG_DIR, CONFIG_FILE_PATH

app = typer.Typer(help="Configuration management.")


@app.command()
def create():
    """Create a base config file."""
    if not config_exists():
        os.makedirs(APP_CONFIG_DIR)
        init_config()
    else:
        if Confirm.ask(
            "You already have a configuration file. Would you like to rewrite it?!"
        ):
            init_config()


@app.command()
def edit():
    """View and modify the config file."""
    if not app_dir_exists() or not config_exists():
        console.print("You don't have any config file. Try `hey config create` first.")
    else:
        subprocess.run([os.environ["EDITOR"], CONFIG_FILE_PATH])
