import pytest
from Exercise_1_unit_testing import bubble_sort_right

def test_bubble_sort_right_correct_sort ():

        input_list = [15,-50,-60,50]

        result = bubble_sort_right(input_list)

        assert result == [-60,-50,15,50]



