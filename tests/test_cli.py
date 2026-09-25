import sys

import pytest
from toolkit.__main__ import main
from toolkit.errors import EmptyExpressionError, InvalidCommandError


def run_cli(*args):
    old_argv = sys.argv
    try:
        sys.argv = ["cli.p", *args]
        main()
    finally:
        sys.argv = old_argv

def test_calculate(capsys):
    run_cli("calc", "2 + 3")

    captured = capsys.readouterr()
    assert captured.out.strip() == '5.0'

def test_calculate_empty(capsys):
    with pytest.raises(EmptyExpressionError):
        run_cli("calc", "")

def test_calculate_invalid(capsys):
    with pytest.raises(InvalidCommandError):
        run_cli("calc", "expression", "4+5")

def test_convert(capsys):
    run_cli("convert", "25", "--from", "c", "--to", "f")

    captured = capsys.readouterr()
    assert captured.out.strip() == '77.0'

def test_convert_invalid(capsys):
    with pytest.raises(InvalidCommandError):
        run_cli("convert", "25", "--", "from", "c", "--" ,"to", "f")