import os
import subprocess
import tempfile

from hey.consts import DEFAULT_EDITOR


def open_tmp_editor() -> str:
    """opens the default editor (`$EDITOR`)

    Returns:
        str: input string
    """

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_file:
        temp_file_path = temp_file.name

    subprocess.run([DEFAULT_EDITOR, temp_file_path])

    with open(temp_file_path, "r") as file:
        data = file.read()

    os.unlink(temp_file_path)
    return data
