import pytest
from toolkit.converter import convert, convert_temperature, is_compatible


def test_unknown_unit_is_compatible():
    with pytest.raises(ValueError):
        is_compatible("kg", "j")


def test_is_compatible():
    assert is_compatible("g", "kg")
    assert is_compatible("c", "k")
    assert is_compatible("mm", "m")


def test_convert_temperature():
    assert convert_temperature("25", "c", "k") == 298.15
    assert convert_temperature("25", "c", "f") == 77


def test_convert_temperature_abs_zero():
    with pytest.raises(ValueError):
        convert_temperature("-273.15", "c", "k")
        convert_temperature("-280", "c", "k")


def test_unknown_unit_convert_temperature():
    with pytest.raises(ValueError):
        convert_temperature("67", "c", "g")


def test_convert():
    assert convert("1000", "m", "km") == 1
    assert convert("25", "c", "k") == 298.15
    assert convert("500", "g", "kg") == 0.5


def test_convert_not_compatible():
    with pytest.raises(ValueError):
        convert("500", "g", "m")
