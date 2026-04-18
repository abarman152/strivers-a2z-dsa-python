import pytest


# -------------------------------
# Largest Element Tests
# -------------------------------
from arrays.easy.arr_001_largest_element import largest_element

@pytest.mark.largest_element
def test_largest_element_basic():
    assert largest_element([3, 3, 6, 1]) == 6
    assert largest_element([3, 3, 0, 99, -40]) == 99


@pytest.mark.largest_element
def test_largest_element_edge_cases():
    assert largest_element([5]) == 5
    assert largest_element([-4, -3, 0, 1, -8]) == 1
    assert largest_element([2, 2, 2]) == 2


@pytest.mark.largest_element
def test_largest_element_invalid():
    with pytest.raises(ValueError):
        largest_element([])
        

# -------------------------------
# Second Largest Element Tests
# -------------------------------


from arrays.easy.arr_002_second_largest import second_largest


@pytest.mark.second_largest
def test_second_largest_basic():
    assert second_largest([8, 8, 7, 6, 5]) == 7
    assert second_largest([1, 2, 3, 4]) == 3


@pytest.mark.second_largest
def test_second_largest_duplicates():
    assert second_largest([10, 10, 10, 10]) == -1
    assert second_largest([7, 7, 2, 2, 10, 10, 10]) == 7


@pytest.mark.second_largest
def test_second_largest_edge_cases():
    # single element
    assert second_largest([5]) == -1

    # two elements
    assert second_largest([2, 1]) == 1

    # all negative
    assert second_largest([-1, -2, -3]) == -2

    # mixed values
    assert second_largest([3, 1, 4, 2]) == 3


@pytest.mark.second_largest
def test_second_largest_large_input():
    nums = list(range(100000))
    assert second_largest(nums) == 99998
    
# -------------------------------
# Check if the array is sorted
# -------------------------------


from arrays.easy.arr_003_check_sorted_array import is_sorted


@pytest.mark.check_sorted_array
def test_sorted():
    assert is_sorted([1, 2, 3, 4, 5]) is True


@pytest.mark.check_sorted_array
def test_not_sorted():
    assert is_sorted([1, 2, 1, 4, 5]) is False


@pytest.mark.check_sorted_array
def test_single_element():
    assert is_sorted([10]) is True


@pytest.mark.check_sorted_array
def test_all_equal():
    assert is_sorted([2, 2, 2, 2]) is True


@pytest.mark.check_sorted_array
def test_descending():
    assert is_sorted([5, 4, 3, 2, 1]) is False


@pytest.mark.check_sorted_array
def test_mixed():
    assert is_sorted([1, 9, 6, 8, 5, 4, 0]) is False