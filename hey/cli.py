"""Console script for hey."""
import argparse
import sys

from constants.informations import APPLICATION_DESCRIPTION, EPILOG_DESCRIPTION, INSTALLATION_GUIDE, VERSION_INFO
from validators.credentials import credentials_validator

from hey import __version__

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
    "--setup",
    type=credentials_validator,
    help="your mindsdb credentials",
)


def main():
    args = parser.parse_args()

    # TODO: check if credentials are valid
    # TODO: check for config file (if exists, override)

    # TODO: deal with ask option
    return 0


if __name__ == "__main__":
    sys.exit(main())
