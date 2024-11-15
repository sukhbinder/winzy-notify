import pytest
import winzy_notify as w

from argparse import Namespace, ArgumentParser

def test_create_parser():
    subparser = ArgumentParser().add_subparsers()
    parser = w.create_parser(subparser)

    assert parser is not None

    result = parser.parse_args(['hello'])
    assert result.msg == ["hello"]
    assert result.title == "Notify"


def test_plugin(capsys):
    w.notify_plugin.hello(None)
    captured = capsys.readouterr()
    assert "Hello! This is an example ``winzy`` plugin." in captured.out
