import json

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


def test_read_configs_returns_user_config_when_valid_json(tmp_path, monkeypatch):
    config_file = tmp_path / "config.json"
    expected = {"model": "gpt-4o-mini"}
    config_file.write_text(json.dumps(expected), encoding="utf-8")

    monkeypatch.setattr(utils, "CONFIG_FILE_PATH", config_file)

    assert utils.read_configs() == expected


def test_read_configs_falls_back_and_shows_create_hint_for_invalid_json(
    tmp_path, monkeypatch
):
    config_file = tmp_path / "config.json"
    config_file.write_text("{broken", encoding="utf-8")

    printed = []

    def fake_print(message):
        printed.append(str(message))

    monkeypatch.setattr(utils, "CONFIG_FILE_PATH", config_file)
    monkeypatch.setattr(utils.console, "print", fake_print)

    assert utils.read_configs() == BASE_CONFIG
    assert any("hey config create" in msg for msg in printed)
