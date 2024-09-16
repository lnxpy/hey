import json
import os

from hey import console
from hey.consts import APP_CONFIG_DIR, BASE_CONFIG, CONFIG_FILE_PATH


def read_configs() -> dict:
    """returns the user-defined config or the base config

    Returns:
        dict: config params
    """

    if os.path.exists(CONFIG_FILE_PATH):
        try:
            with open(CONFIG_FILE_PATH) as file:
                return json.loads(file.read())
        except json.JSONDecodeError as e:
            error_message = (
                f"Your config file is [red bold]broken[/red bold]. "
                f"Try `hey config edit` or `hey config init`. {e}"
            )
            console.print(error_message)
            console.print("Using the [green bold]default settings[/green bold].")

    return BASE_CONFIG


def init_config():
    with open(CONFIG_FILE_PATH, "w+") as conf_file:
        conf_file.write(json.dumps(BASE_CONFIG, indent=4))


def app_dir_exists() -> bool:
    return os.path.exists(APP_CONFIG_DIR)


def config_exists() -> bool:
    return os.path.exists(CONFIG_FILE_PATH)
