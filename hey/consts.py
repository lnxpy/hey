import os
import platform

from platformdirs import user_config_path

# App name
APP_NAME = "Hey"

# Service address
SERVICE_URL = "https://llm.mdb.ai"

if platform.system().lower() == "windows":
    DEFAULT_EDITOR = os.environ.get("EDITOR", "notepad")
else:
    DEFAULT_EDITOR = os.environ.get("EDITOR", "vim")

# basic configuration setup
BASE_CONFIG = {
    "model": "gpt-3.5-turbo",
    "prompt": "Answer in a helpful way.",
    "code_block_theme": "github-light",
    "loading_text": "Thinking..",
    "loading_spinner": "dots",
    "never_style": False,
}

APP_CONFIG_DIR = user_config_path(APP_NAME)
CONFIG_FILE_PATH = APP_CONFIG_DIR / "config.json"
