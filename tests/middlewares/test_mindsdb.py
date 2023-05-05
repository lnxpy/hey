import pytest

from pandas import DataFrame
from unittest.mock import patch, MagicMock
from hey.exceptions.auth import CredentialsError
from hey.exceptions.connection import NetworkError
from requests.exceptions import HTTPError, ConnectionError

from hey.constants.service import MINDSDB_HOST
from hey.middlewares.mindsdb import MindsDB


@patch('mindsdb_sdk.connect')
def test_authenticate(mock_connect):
    email = 'test@test.com'
    password = 'testpassword'

    mock_server = MagicMock()
    mock_connect.return_value = mock_server

    mindsdb = MindsDB(email, password)

    mindsdb.authenticate()

    mock_connect.assert_called_once_with(MINDSDB_HOST, login=email, password=password)
    mock_server.list_databases.assert_called_once()

    assert mindsdb.is_authenticated is True


def test_authenticate_incorrect_password():
    mindsdb = MindsDB('test@test.com', 'testpassword')

    with pytest.raises(CredentialsError):
        with patch('mindsdb_sdk.connect', side_effect=HTTPError):
            mindsdb.authenticate()


def test_authenticate_network_error():
    mindsdb = MindsDB('test@test.com', 'testpassword')

    with pytest.raises(NetworkError):
        with patch('mindsdb_sdk.connect', side_effect=ConnectionError):
            mindsdb.authenticate()


def test_mindsdb_answer_exception():
    mock_database = MagicMock(spec=DataFrame)
    mock_database.query.return_value.fetch.return_value = [['test answer']]

    email = 'test@test.com'
    password = 'testpassword'
    mindsdb = MindsDB(email, password)
    mindsdb.database = mock_database

    mock_database.query.side_effect = Exception
    with pytest.raises(Exception):
        mindsdb.answer('test question')
