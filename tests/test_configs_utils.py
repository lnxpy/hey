import json
from pathlib import Path

from hey.configs import utils
from hey.consts import BASE_CONFIG


def test_init_config_creates_directory_and_file(tmp_path, monkeypatch):
    config_dir = tmp_path / "hey"
    config_file = config_dir / "config.json"

    monkeypatch.setattr(utils, "APP_CONFIG_DIR", config_dir)
    monkeypatch.setattr(utils, "CONFIG_FILE_PATH", config_file)

    utils.init_config()

    assert config_file.exists()
    loaded = json.loads(config_file.read_text(encoding="utf-8"))
    assert loaded == BASE_CONFIG
