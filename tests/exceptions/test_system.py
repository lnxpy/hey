import pytest
from hey.exceptions.system import (
    EmailEnvVarNotExists,
    BrokenCredentials, 
    KeyringIssue,
)


def test_email_env_var_not_exists_exception():
    with pytest.raises(EmailEnvVarNotExists):
        raise EmailEnvVarNotExists("Email environment variable not set.")

def test_broken_credentials_exception():
    with pytest.raises(BrokenCredentials):
        raise BrokenCredentials("Invalid or broken credentials provided.")

def test_keyring_issue_exception():
    with pytest.raises(KeyringIssue):
        raise KeyringIssue("Keyring service failed to execute.")
