"""
Problem:
Remove Duplicates from Sorted Array

Given a sorted array nums, remove duplicates in-place such that each unique element
appears only once. Return the number of unique elements (k).

Modify nums so that the first k elements contain the unique values.

Examples:
Input: [0, 0, 3, 3, 5, 6]
Output: 4
Modified nums: [0, 3, 5, 6, _, _]

Input: [-2, 2, 4, 4, 4, 4, 5, 5]
Output: 4
Modified nums: [-2, 2, 4, 5, _, _, _, _]

Intuition:
Since the array is sorted, duplicates are adjacent.
Use two pointers to overwrite duplicates.

Optimal Approach:
- Use pointer `k` to track position of unique elements
- Traverse array from index 1
- If current != previous unique → place it at index k and increment k

Time Complexity: O(n)
Space Complexity: O(1)

Edge Cases:
- Single element
- All elements same
- Negative numbers
"""

def remove_duplicates(nums):
    if not nums:
        return 0

    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1

    return k