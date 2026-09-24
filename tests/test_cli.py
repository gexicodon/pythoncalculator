import pytest
import sys
from toolkit.__main__ import main
from toolkit.errors import EmptyExpressionError, InvalidCommandError

'''
def test_calc(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        ["toolkit", "calc", "2 + 3"],
    )

    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "5"

def test_conv(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        ["toolkit", "convert", "1", "--from", "kg", "--to", "g"]
    )

    main()
    captured = capsys.readouterr()
    assert (captured.out.strip() == "1000" or captured.out.strip() == '1000.0')

'''