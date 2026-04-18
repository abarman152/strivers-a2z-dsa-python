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