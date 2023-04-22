"""
this file contains custom exceptions that might happen during the regular system calling
"""


class EmailEnvVarNotExists(Exception): ...


class BrokenCredentials(Exception): ...


class KeyringIssue(Exception): ...
