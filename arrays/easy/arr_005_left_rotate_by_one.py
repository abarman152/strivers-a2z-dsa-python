"""
Problem:
Left Rotate Array by One

Given an integer array nums, rotate the array to the left by one in-place.

Examples:
Input: [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]

Input: [-1, 0, 3, 6]
Output: [0, 3, 6, -1]

Input: [7, 6, 5, 4]
Output: [6, 5, 4, 7]

Intuition:
Store the first element and shift all elements one position to the left,
then place the first element at the end.

Optimal Approach:
- Save first element
- Shift elements left
- Place saved element at last index

Time Complexity: O(n)
Space Complexity: O(1)

Edge Cases:
- Single element → no change
- Negative values
"""

def left_rotate_by_one(nums):
    n = len(nums)
    if n <= 1:
        return

    first = nums[0]

    for i in range(1, n):
        nums[i - 1] = nums[i]

    nums[n - 1] = first