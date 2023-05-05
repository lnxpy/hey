import pytest

from hey.exceptions.connection import NetworkError


def test_network_error():
    with pytest.raises(NetworkError):
        raise NetworkError("Connection lost")
