"""
Problem:
Check if the Array is Sorted II

Given an array nums of n integers, return True if the array is sorted
in non-decreasing order, otherwise return False.

Examples:
Input: [1, 2, 3, 4, 5]
Output: True

Input: [1, 2, 1, 4, 5]
Output: False

Input: [1, 9, 6, 8, 5, 4, 0]
Output: False

Intuition:
A sorted array must satisfy nums[i] <= nums[i+1] for all valid indices.

Optimal Approach:
- Traverse the array once
- If any nums[i] > nums[i+1], return False
- Otherwise return True

Time Complexity: O(n)
Space Complexity: O(1)

Edge Cases:
- Single element → always True
- All elements equal
"""

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True