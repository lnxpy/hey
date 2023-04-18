

class Authentication:
    """
    MindsDB authentication manager class
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

    def is_authenticated(self):
        return True
