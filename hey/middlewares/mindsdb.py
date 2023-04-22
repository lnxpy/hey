from typing import Union

import mindsdb_sdk
from mindsdb_sdk.server import Server
from requests.exceptions import HTTPError, ConnectionError

from hey.constants.service import MINDSDB_HOST
from hey.exceptions.auth import CredentialsError
from hey.exceptions.connection import NetworkError


class User:
    """
    MindsDB user auth manager class
    """

    def __init__(self, email: str, password: str) -> None:
        """
        initializer class.
        Args:
            email: MindsDB account email address
            password: MindsDB account password
        """
        self.email = email
        self.password = password

        self.is_authenticated: bool = False

    def authenticate(self) -> Union[Server, None]:
        """
        authorizes the email and password with MindsDB's host
        Returns:
            user object
        """
        try:
            user = mindsdb_sdk.connect(
                MINDSDB_HOST,
                login=self.email,
                password=self.password,
            )
        except HTTPError:
            raise CredentialsError('Email or password is incorrect. Make sure to enter the right credentials.')
        except ConnectionError:
            raise NetworkError('Make sure you have access to the connection and try again.')

        self.is_authenticated = True
        return user
