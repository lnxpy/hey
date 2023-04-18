import re
from argparse import ArgumentTypeError

from typing import Union


def credentials_validator(phrase: str) -> Union[dict, None]:
    """
    argparse validator for `--setup` option that matches the
    credential phrase with <email>:<password> pattern.

    Examples:
        abcd@somewhere.com:password123
        somewhere@something.com:testpass123

    Args:
        phrase: credentials phrase

    Returns:
        email and password if well-patterned
    """
    if re.match(r"\S+@\S+:\S+", phrase):
        email, password = phrase.split(':')
        return {
            'email': email,
            'password': password,
        }
    else:
        raise ArgumentTypeError('Credentials pattern is not acceptable. You have to use <email>:<password> pattern ('
                                'e.g. abc@def.com:testpass123).')
