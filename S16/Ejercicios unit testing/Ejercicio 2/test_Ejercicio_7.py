import pytest

from Ejercicio_7 import order_words

def test_check_order_words_correct_order():
    words = "hoja-papel-lapiz"

    result = order_words(words)

    assert result == "hoja-lapiz-papel"


def test_check_order_words_correct_order_1():
    words = "ola-mar-arena"

    result = order_words(words)

    assert result == "arena-mar-ola"

def test_check_order_words_correct_order_2():
    words = "agua-aguja-aceite"

    result = order_words(words)

    assert result == "aceite-agua-aguja"