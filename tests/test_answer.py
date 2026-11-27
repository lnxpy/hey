from unittest.mock import patch

from rich.panel import Panel

from hey.openai import answer


@patch("hey.openai.ChatGPT")
def test_answer_no_style_returns_raw_text(mock_chatgpt):
    mock_chatgpt.return_value.ask.return_value = "raw answer"

    result = answer("question", no_style=True)

    assert result == "raw answer"


@patch("hey.openai.ChatGPT")
def test_answer_styled_returns_panel(mock_chatgpt):
    mock_chatgpt.return_value.ask.return_value = "raw answer"

    result = answer("question", no_style=False)

    assert isinstance(result, Panel)
