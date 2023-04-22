import argparse
import os
import sys

from hey import __version__
from hey.accounts.auth import User
from hey.constants.informations import APPLICATION_DESCRIPTION, EPILOG_DESCRIPTION, INSTALLATION_GUIDE, VERSION_INFO
from hey.constants.service import SERVICE_NAME
from hey.exceptions.system import EmailEnvVarNotExists, BrokenCredentials
from hey.validators.credentials import credentials_validator

import keyring


parser = argparse.ArgumentParser(
    description=APPLICATION_DESCRIPTION + '\n\r\n\r' + INSTALLATION_GUIDE,
    epilog=EPILOG_DESCRIPTION,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

parser.add_argument(
    '--version',
    action='version',
    version=VERSION_INFO.format(__version__),
)

parser.add_argument(
    'ask',
    nargs='*',
    help='ask what you need',
)

parser.add_argument(
    '--set-password',
    type=str,
    help='set your mindsdb account password',
    metavar='',
)


def main():
    args = parser.parse_args()

    if args.set_password:
        email_address = os.environ.get('HEY_EMAIL_ADDRESS')
        if email_address:
            keyring.set_password(
                service_name=SERVICE_NAME.lower(),
                username=email_address,
                password=args.set_password,
            )
        else:
            raise EmailEnvVarNotExists('Make sure you have defined HEY_EMAIL_ADDRESS environment variable properly.')

    credentials = keyring.get_credential(
        service_name=SERVICE_NAME.lower(),
        username=os.environ.get('HEY_EMAIL_ADDRESS'),
    )

    if not credentials:
        raise BrokenCredentials(
            'Make sure you have set your HEY_EMAIL_ADDRESS and password via --set-password.'
        )

    if args.ask:
        # TODO: Refactor User class to Connection class
        user = User(
            email=credentials.username,
            password=credentials.password
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
