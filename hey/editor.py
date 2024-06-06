import os
import subprocess
import tempfile

from rich.console import Console

logger = Console()


def open_tmp_editor() -> str:
    """opens the default editor (`$EDITOR`)

    Returns:
        str: input string
    """

    with tempfile.NamedTemporaryFile(mode="w+") as temp_file:
        temp_file_path = temp_file.name

        subprocess.run([os.environ["EDITOR"], temp_file_path])

        with open(temp_file_path, "r") as file:
            data = file.read()

        return data
