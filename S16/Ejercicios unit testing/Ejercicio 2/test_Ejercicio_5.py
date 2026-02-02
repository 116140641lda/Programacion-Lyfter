import pytest

from Ejercicio_5 import reverse_string

def test_check_Ejercicio_5_correct_reverse():
        input_sentence = "Oracion"

        result = reverse_string(input_sentence)

        assert result == "noicarO"