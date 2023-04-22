import mindsdb_sdk
from mindsdb_sdk.server import Server, Database
from pandas import DataFrame
from requests.exceptions import HTTPError, ConnectionError
from rich.markdown import Markdown

from hey.constants.service import MINDSDB_HOST
from hey.exceptions.auth import CredentialsError
from hey.exceptions.connection import NetworkError


def to_data(dataframe: DataFrame) -> str:
    """
    takes a pandas dataframe and returns the first value from the first column
    Args:
        dataframe:

    Returns:
        first value of the first column of dataframe that GPT responses
    """
    return dataframe.iloc[:, 0].values[0]


class MindsDB:
    """
    MindsDB manager class
    """

    SQL_ASKING_QUERY = '''
    SELECT response
    FROM mindsdb.gpt_model
    WHERE author_username = "mindsdb"
    AND text = "{}";
    '''

    def __init__(self, email: str, password: str) -> None:
        """
        initializer class.
        Args:
            email: MindsDB account email address (that is stored as an env var)
            password: MindsDB account password
        """
        self.email = email
        self.password = password

        self.is_authenticated: bool = False
        self.database: Database

    def authenticate(self) -> None:
        """
        authorizes the email and password with MindsDB's host
        Returns:
            server object
        """

        try:
            server = mindsdb_sdk.connect(
                MINDSDB_HOST,
                login=self.email,
                password=self.password,
            )
        except HTTPError:
            raise CredentialsError('Email or password is incorrect. Make sure to enter the right credentials.')
        except ConnectionError:
            raise NetworkError('Make sure you have access to the internet and try again.')

        self.is_authenticated = True
        self.database = self.collect_database(server)

    @staticmethod
    def collect_database(server: Server) -> Database:
        return server.list_databases()[0]

    def answer(self, question: str) -> Markdown:
        """
        takes the question and queries then converts the response into `rich.Markdown`
        Args:
            question: 

        Returns:

        """
        return Markdown(to_data(
            self.database.query(
                MindsDB.SQL_ASKING_QUERY.format(question)
            ).fetch()
        ))
