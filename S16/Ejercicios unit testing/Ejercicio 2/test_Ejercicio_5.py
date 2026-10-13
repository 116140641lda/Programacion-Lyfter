import pytest

from Ejercicio_5 import reverse_string

def test_check_Ejercicio_5_correct_reverse():
        input_sentences = "Oracion"

        result = reverse_string(input_sentences)

        assert result == "noicarO"


def test_check_Ejercicio_5_correct_reverse_1():
        input_sentences = "Sentence"

        result = reverse_string(input_sentences)

        assert result == "ecnetneS"


def test_check_Ejercicio_5_correct_reverse_2():
        input_sentences = "Hi"

        result = reverse_string(input_sentences)

        assert result == "iH"