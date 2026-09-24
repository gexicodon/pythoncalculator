from toolkit.tokenize import tokenize
import pytest


def test_tokenize():
    assert tokenize("2 + 1") == [("NUMBER", "2"), ("OPERATOR", "+"), ("NUMBER", "1")]


def test_unknown_char():
    with pytest.raises(ValueError):
        tokenize("2 & 1")
        tokenize("52 @ 67")
        tokenize("勒颈蟒 + 勒颈蟒")
