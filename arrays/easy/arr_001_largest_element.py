"""
Problem: Largest Element in Array
Platform: TUF / GFG
Pattern: Array Traversal

--------------------------------------------------
Problem Statement:
Given an array of integers nums, return the largest element.

Examples:
Input: [3, 3, 6, 1]
Output: 6

Input: [3, 3, 0, 99, -40]
Output: 99

--------------------------------------------------
Intuition:
We need to find the maximum value.
Traverse the array and keep updating the maximum.

--------------------------------------------------
Approach:
1. Initialize max_val with first element
2. Traverse array
3. Update max_val if current element is greater

--------------------------------------------------
Complexity:
Time: O(n)
Space: O(1)

--------------------------------------------------
Edge Cases:
- Single element array
- All negative numbers
- Duplicate elements
"""

def largest_element(nums):
    if not nums:
        raise ValueError("Input array cannot be empty")

    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num

    return max_val