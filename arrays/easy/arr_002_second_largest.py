"""
ID: ARR_002
Problem: Second Largest Element in Array
Topic: Arrays
Difficulty: Easy

--------------------------------------------------
Problem Statement:
Given an array of integers nums, return the second largest element.
If the second largest element does not exist, return -1.

--------------------------------------------------
Examples:
Input: [8, 8, 7, 6, 5]
Output: 7

Input: [10, 10, 10, 10]
Output: -1

--------------------------------------------------
Intuition:
We extend the "largest element" problem.

Instead of tracking only the maximum,
we track:
1. largest
2. second largest

--------------------------------------------------
Approach (Optimal - Single Pass):

Initialize:
    largest = -inf
    second_largest = -inf

Traverse array:
    If current > largest:
        second_largest = largest
        largest = current

    Else if:
        largest > current > second_largest:
        update second_largest

Return:
    second_largest if exists else -1

--------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(1)

--------------------------------------------------
Edge Cases:
- Array size < 2 → return -1
- All elements same → return -1
- Negative values
- Duplicates
"""


def second_largest(nums):
    """
    Returns the second largest element in the array.
    If not present, returns -1.
    """

    if len(nums) < 2:
        return -1

    largest = float("-inf")
    second_largest_val = float("-inf")

    for num in nums:
        if num > largest:
            second_largest_val = largest
            largest = num
        elif largest > num > second_largest_val:
            second_largest_val = num

    return second_largest_val if second_largest_val != float("-inf") else -1


# Optional: local quick test (not used by pytest)
if __name__ == "__main__":
    sample = [7, 7, 2, 2, 10, 10, 10]
    print("Second Largest:", second_largest(sample))  # Expected: 7