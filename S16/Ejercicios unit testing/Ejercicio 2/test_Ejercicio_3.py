import pytest

from Ejercicio_3 import change_const_var

def test_check_Ejercicio_3_correct_const_var():
        constant = 15

        result = change_const_var(constant)

        assert result == 16

    

def test_check_Ejercicio_3_correct_const_var_2():
        constant = 200

        result = change_const_var(constant)

        assert result == 201


def test_check_Ejercicio_3_correct_const_var_3():
        constant = -2

        result = change_const_var(constant)

        assert result == -1