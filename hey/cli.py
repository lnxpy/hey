"""Console script for hey."""
import argparse
import sys

from hey import __version__
from hey.accounts.auth import User
from hey.constants.informations import APPLICATION_DESCRIPTION, EPILOG_DESCRIPTION, INSTALLATION_GUIDE, VERSION_INFO
from hey.validators.credentials import credentials_validator

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
    type=str,
    nargs='*',
    help='ask what you need',
)

parser.add_argument(
    "--auth",
    type=credentials_validator,
    help="your mindsdb authenticating credentials in <email>:<password> pattern (e.g. abc@def.com:testpass)",
)


def main():
    args = parser.parse_args()

    if args.auth:
        # TODO: Refactor User class to Connection class
        user = User(**args.auth)
        user.authenticate()

    # TODO: check for config file (if exists, override)
    # TODO: deal with ask option

    return 0


if __name__ == "__main__":
    sys.exit(main())
