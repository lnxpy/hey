import time

import keyring
from openai import OpenAI, OpenAIError
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from hey.configs import configs
from hey.consts import BASE_CONFIG, HEY_TOKEN
from hey.exceptions import ConnectionIssue, TokenIsNotDefined


class Auth:
    def __init__(self) -> None:
        self.is_valid = False

    def validate(self) -> str:
        token = keyring.get_password("system", HEY_TOKEN)
        if token:
            self.is_valid = True
            return token
        raise TokenIsNotDefined(
            "token is not defined, Use `hey auth` to set the token."
        )


class ChatGPT:
    def __init__(
        self,
        model=configs.get("model", BASE_CONFIG["model"]),
        prompt=configs.get("prompt", BASE_CONFIG["prompt"]),
        auth: Auth = None,
    ) -> None:
        self.auth = auth or Auth()
        self.token = self.auth.validate()
        self.model = model
        self.prompt = prompt

    def ask(self, text: str) -> str:
        if not text:
            raise ValueError("provide a valid input.")
        try:
            client_mindsdb_serve = OpenAI(
                api_key=self.token,
                base_url=configs.get("service", BASE_CONFIG["service"]),
            )
            chat_completion_gpt = client_mindsdb_serve.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": self.prompt,
                    },
                    {"role": "user", "content": text},
                ],
                model=self.model,
            )
            return chat_completion_gpt.choices[0].message.content
        except OpenAIError:
            raise ConnectionIssue("an error occurred while calling the API endpoint.")


def answer(question: str, no_style: bool) -> str | Panel:
    """interface between commands and ChatGPT

    Args:
        question (str): question phrase
        no_style (bool): whether returning in a panel or not

    Returns:
        str | Panel: solid raw result or paneled
    """

    with Console().status(
        configs.get("loading_text", BASE_CONFIG["loading_text"]),
        spinner=configs.get("loading_spinner", BASE_CONFIG["loading_spinner"]),
    ):
        start_time = time.time()
        c = ChatGPT()
        result = Markdown(
            c.ask(question),
            code_theme=configs.get("code_block_theme", BASE_CONFIG["code_block_theme"]),
        )
        end_time = time.time()

    if no_style:
        return result
    else:
        paneled = Panel(
            result,
            border_style="green",
            title=":sparkles:",
            subtitle=f"~{end_time-start_time:.1f}s",
            subtitle_align="right",
            title_align="left",
        )
        return paneled
