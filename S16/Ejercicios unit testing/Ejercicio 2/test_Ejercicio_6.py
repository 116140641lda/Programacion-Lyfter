import pytest

from Ejercicio_6 import count_may_min

def test_check_count_may_min_correct_count_letter_1():
    text = "Hola Mundo"

    result = count_may_min(text)

    assert result == (2,7)


def test_check_count_may_min_correct_count_letter_2():
    text = "Cuenta MIS Letras"

    result = count_may_min(text)

    assert result == (5,10)


def test_check_count_may_min_correct_count_letter_3():
    text = "Cuenta MIS Letras"

    result = count_may_min(text)

    assert result == (5,10)