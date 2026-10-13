import random

from Exercise_1_unit_testing import bubble_sort_left

def test_big_len_exercise_1_unit_testing_correct_sort():
    input_list = random.sample(range(200), 150)

    correct_sort = sorted( input_list, reverse=True)

    result = bubble_sort_left(input_list)

    assert result == correct_sort


