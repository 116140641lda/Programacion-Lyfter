import pytest

from Exercise_1_unit_testing import bubble_sort_right

def empty_list_bubble_sort_right_correct_sort ():
    input_list = []

    result = bubble_sort_right[input_list]

    assert result == []


