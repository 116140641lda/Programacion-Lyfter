from math_utilities import sum_list_items

def test_sum_list_items_sums_all_items_correctly():

    # ARRANGE
    list_input = [3,7,8]

    result = sum_list_items(list_input)

    assert result == 18