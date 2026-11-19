import pytest

from inflect import BadNumValueError, engine


def test_number_to_words_raises_for_inf():
    p = engine()
    with pytest.raises(BadNumValueError):
        p.number_to_words(float("inf"))


def test_number_to_words_raises_for_neg_inf():
    p = engine()
    with pytest.raises(BadNumValueError):
        p.number_to_words(float("-inf"))


def test_number_to_words_raises_for_nan():
    p = engine()
    with pytest.raises(BadNumValueError):
        p.number_to_words(float("nan"))


def test_number_to_words_raises_for_decimal_inf():
    from decimal import Decimal

    p = engine()
    with pytest.raises(BadNumValueError):
        p.number_to_words(Decimal("Infinity"))


def test_number_to_words_raises_for_decimal_nan():
    from decimal import Decimal

    p = engine()
    with pytest.raises(BadNumValueError):
        p.number_to_words(Decimal("NaN"))
