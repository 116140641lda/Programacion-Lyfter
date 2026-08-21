import pytest

from Exercise_1_unit_testing import bubble_sort_right

def test_no_list_bubble_sort_right_not_a_list ():
    with pytest.raises(ValueError, match="Debe ser una lista"):
        bubble_sort_right("no lista")