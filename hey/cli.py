import argparse
import os
import sys
from getpass import getpass

import keyring
from rich.console import Console

from hey import __version__
from hey.constants.informations import APPLICATION_DESCRIPTION
from hey.constants.informations import EPILOG_DESCRIPTION
from hey.constants.informations import INSTALLATION_GUIDE
from hey.constants.informations import VERSION_INFO
from hey.constants.service import SERVICE_NAME
from hey.constants.system import LOCAL_EMAIL_ADDRESS_VARIABLE_NAME
from hey.exceptions.system import BrokenCredentials
from hey.exceptions.system import EmailEnvVarNotExists
from hey.exceptions.system import KeyringIssue
from hey.middlewares.mindsdb import MindsDB

parser = argparse.ArgumentParser(
    description=APPLICATION_DESCRIPTION + '\n\r\n\r' + INSTALLATION_GUIDE,
    epilog=EPILOG_DESCRIPTION,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    prog='hey',
)

parser.add_argument(
    'ask',
    nargs='*',
    help='ask what you need',
)

parser.add_argument(
    '--version',
    action='version',
    version=VERSION_INFO.format(__version__),
)

parser.add_argument(
    '--auth',
    action='store_true',
    help='set your mindsdb account password',
)


def main():
    args = parser.parse_args()
    console = Console()

    if args.auth:
        email_address = os.environ.get(LOCAL_EMAIL_ADDRESS_VARIABLE_NAME)
        password = getpass(f'Password for ({email_address}):')
        if email_address:
            try:
                keyring.set_password(
                    service_name=KEYRING_SERVICE_NAME.lower(),
                    username=email_address,
                    password=password,
                )
            except Exception as _:
                raise KeyringIssue(
                    'There is something wrong with your OS keyring system. Make sure you have right access to run hey '
                    'on your system. '
                )
            console.print(f'Password successfully set for {email_address}!')
        else:
            raise EmailEnvVarNotExists(f'Make sure you have defined {LOCAL_EMAIL_ADDRESS_VARIABLE_NAME} environment '
                                       f'variable properly.')

    credentials = keyring.get_credential(
        service_name=KEYRING_SERVICE_NAME.lower(),
        username=os.environ.get(LOCAL_EMAIL_ADDRESS_VARIABLE_NAME),
    )

    if not credentials:
        raise BrokenCredentials(
            f'Make sure you have set your {LOCAL_EMAIL_ADDRESS_VARIABLE_NAME} and password via --auth.'
        )

    if args.ask:
        with console.status('Creating instance..'):
            instance = MindsDB(
                email=credentials.username,
                password=credentials.password
            )

        with console.status('Authenticating..', spinner='dots2'):
            instance.authenticate()

        with console.status('Hey is typing..'):
            console.print(instance.answer(
                ' '.join(args.ask)
            ))

    return 0


if __name__ == "__main__":
    sys.exit(main())
