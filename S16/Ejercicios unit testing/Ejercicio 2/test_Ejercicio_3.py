import pytest

from Ejercicio_3 import change_const_var

def test_check_Ejercicio_3_correct_const_var():
        constant = 15

        result = change_const_var(constant)

        assert result == 16