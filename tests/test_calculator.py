from toolkit.calculation import calc, infix_to_postfix, priority
import pytest


def test_priority():
    assert priority(("OPERATOR", "*")) > priority(("OPERATOR", "+"))


def test_infix_to_postfix():
    assert infix_to_postfix([("NUMBER", "2"), ("OPERATOR", "+"), ("NUMBER", "3")]) == [
        ("NUMBER", "2"),
        ("NUMBER", "3"),
        ("OPERATOR", "+"),
    ]


def test_calc():
    assert calc([("NUMBER", "2"), ("NUMBER", "3"), ("OPERATOR", "*")]) == 6
    assert (
        calc(
            [
                ("NUMBER", "2"),
                ("OPERATOR", "neg"),
                ("NUMBER", "3"),
                ("OPERATOR", "neg"),
                ("OPERATOR", "*"),
            ]
        )
        == 6
    )


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc([("NUMBER", "2"), ("NUMBER", "0"), ("OPERATOR", "/")])


def test_passed_operand():
    with pytest.raises(Exception):
        calc([("NUMBER", "2"), ("OPERATOR", "+")])
