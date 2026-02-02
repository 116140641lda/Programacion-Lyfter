import pytest

from Ejercicio_4 import sum_numbers

def test_check_Ejercicio_4_correct_sum():
        sum_num = (1,5,10,15)

        result = sum_numbers(sum_num)

        assert result == 31