from hey.cli import parser


def test_argparse():
    args = parser.parse_args([])
    assert args.ask == []

    args = parser.parse_args(['capital', 'France'])
    assert args.ask == ['capital', 'France']


def test_set_password_parser():
    pass