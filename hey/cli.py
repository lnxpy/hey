import argparse
import os
import sys

import keyring
from rich.console import Console

from hey import __version__
from hey.constants.informations import APPLICATION_DESCRIPTION, EPILOG_DESCRIPTION, INSTALLATION_GUIDE, VERSION_INFO
from hey.constants.service import SERVICE_NAME
from hey.constants.system import LOCAL_EMAIL_ADDRESS_VARIABLE_NAME
from hey.exceptions.system import BrokenCredentials, EmailEnvVarNotExists, KeyringIssue
from hey.middlewares.mindsdb import MindsDB

parser = argparse.ArgumentParser(
    description=APPLICATION_DESCRIPTION + '\n\r\n\r' + INSTALLATION_GUIDE,
    epilog=EPILOG_DESCRIPTION,
    formatter_class=argparse.RawDescriptionHelpFormatter,
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
    '--set-password',
    type=str,
    help='set your mindsdb account password',
    metavar='',
)


def main():
    args = parser.parse_args()
    console = Console()

    if args.set_password:
        email_address = os.environ.get(LOCAL_EMAIL_ADDRESS_VARIABLE_NAME)
        if email_address:
            try:
                keyring.set_password(
                    service_name=SERVICE_NAME.lower(),
                    username=email_address,
                    password=args.set_password,
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
        service_name=SERVICE_NAME.lower(),
        username=os.environ.get(LOCAL_EMAIL_ADDRESS_VARIABLE_NAME),
    )

    if not credentials:
        raise BrokenCredentials(
            f'Make sure you have set your {LOCAL_EMAIL_ADDRESS_VARIABLE_NAME} and password via --set-password.'
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
