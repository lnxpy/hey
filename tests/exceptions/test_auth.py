import pytest 

from hey.exceptions.auth import CredentialsError


def test_credentials_error():
    with pytest.raises(CredentialsError):
        raise CredentialsError("Invalid credentials.")
