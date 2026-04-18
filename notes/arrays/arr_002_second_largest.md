# ARR_002 - Second Largest Element in Array

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Topic-Arrays-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Solved-success?style=flat-square" />
</p>

---

## Problem Statement

Given an array of integers, return the **second largest distinct element**.

- The second largest is the largest value strictly less than the maximum.
- If all elements are identical, or if the array has fewer than 2 distinct values, return `-1`.
- Duplicates of the largest element do not count as the second largest.

```
Input:  [1, 2, 4, 7, 7, 5]     Output: 5
Input:  [7, 7, 7]               Output: -1
Input:  [1]                     Output: -1
Input:  [-3, -1, -4, -2]        Output: -2
```

---

## Key Insight

The answer requires finding the largest value that is **not equal to the maximum**.
Sorting achieves this but does unnecessary work — it orders every element when you only need two values.
Tracking `largest` and `second_largest` as two variables lets you find the answer in a single pass, which is the theoretical minimum for this problem.

---

## Approaches

### Brute Force — Sorting

**Logic:**
1. Sort the array in ascending order — largest element is now at `nums[-1]`.
2. Traverse backward from the second-to-last index.
3. Return the first element that is **not equal** to the largest.
4. If no such element exists, return `-1`.

**Why it works:**
After sorting, all elements are ordered. Walking backward from the end skips duplicates of the maximum and lands on the second largest distinct value.

**Why it is not optimal:**
Sorting solves a harder problem (full ordering) than required. The extra O(n log n) work is wasted when only two values are needed.

```python
def second_largest_brute(nums: list[int]) -> int:
    nums_sorted = sorted(nums)
    largest = nums_sorted[-1]

    for i in range(len(nums_sorted) - 2, -1, -1):
        if nums_sorted[i] != largest:
            return nums_sorted[i]

    return -1
```

| Complexity | Value |
|---|---|
| Time | O(n log n + n) |
| Space | O(n) — sorted copy |

---

### Better Approach — Two Pass

**Logic:**
- **Pass 1:** Traverse the entire array to find `largest = max(nums)`.
- **Pass 2:** Traverse again to find the maximum value among all elements that are **strictly less than** `largest`.
- If no such value exists, return `-1`.

**Why it improves over brute force:**
Eliminates the sort entirely. Two linear scans = O(2n), which is strictly better than O(n log n).

```python
def second_largest_better(nums: list[int]) -> int:
    largest = max(nums)
    second = -1

    for num in nums:
        if num != largest:
            second = max(second, num)

    return second
```

> Note: Initializing `second` to `-1` works when values are non-negative. For arrays that may contain all negative values, initialize `second` to `float('-inf')` and return `-1` explicitly if it remains unchanged.

```python
def second_largest_better(nums: list[int]) -> int:
    largest = max(nums)
    second = float('-inf')

    for num in nums:
        if num != largest:
            second = max(second, num)

    return second if second != float('-inf') else -1
```

| Complexity | Value |
|---|---|
| Time | O(n + n) = O(2n) |
| Space | O(1) |

---

### Optimal Approach — Single Pass

**Logic:**
Maintain two variables simultaneously: `largest` and `second_largest`.

Update rules on each element `num`:

```
if num > largest:
    second_largest = largest      # old largest becomes second
    largest = num                 # new largest takes over

elif num < largest and num > second_largest:
    second_largest = num          # valid candidate for second place
```

Duplicates of `largest` are silently skipped by the `num > largest` and `num < largest` conditions — neither branch fires when `num == largest`.

**Why this is optimal:**
A single traversal, two scalar variables, no mutation of the input. This cannot be done faster — every element must be seen at least once.

| Complexity | Value |
|---|---|
| Time | O(n) |
| Space | O(1) |

---

## Visualization

```
Input: [1, 2, 4, 7, 7, 5]

Init     →  largest = -inf,  second = -inf

num = 1  →  1 > -inf   →  second = -inf,  largest = 1
num = 2  →  2 > 1      →  second = 1,     largest = 2
num = 4  →  4 > 2      →  second = 2,     largest = 4
num = 7  →  7 > 4      →  second = 4,     largest = 7
num = 7  →  7 == 7     →  no update       (duplicate skipped)
num = 5  →  5 < 7, 5 > 4  →  second = 5, largest = 7

Output   →  5
```

```
Input: [7, 7, 7]

Init     →  largest = -inf,  second = -inf

num = 7  →  7 > -inf   →  second = -inf,  largest = 7
num = 7  →  7 == 7     →  no update
num = 7  →  7 == 7     →  no update

second = -inf  →  Output: -1
```

```
Input: [-3, -1, -4, -2]

Init      →  largest = -inf,  second = -inf

num = -3  →  -3 > -inf   →  second = -inf,  largest = -3
num = -1  →  -1 > -3     →  second = -3,    largest = -1
num = -4  →  -4 < -1, -4 < -3  →  no update
num = -2  →  -2 < -1, -2 > -3  →  second = -2, largest = -1

Output    →  -2
```

---

## Pattern Recognition

**Tags:** `#array` `#traversal` `#max_tracking` `#two_variable_tracking` `#single_pass`

**Relationship to ARR_001:**
This is a direct extension of "Largest Element in Array". That problem tracks one variable; this tracks two. The update logic follows the same running-best principle.

**When to use this pattern:**
- Any problem requiring the top-k values without full sorting (k = 2 here).
- Situations where you need to maintain a small fixed set of "best seen so far" values.
- Problems where mutating or sorting the input is not allowed.

**Related problems:**
- Third largest element (extend to three variables)
- Kth largest element (generalize with a min-heap of size k)
- Maximum and minimum in a single pass
- Kadane's Algorithm (same running-best structure, applied to subarrays)

---

## Edge Cases

| Case | Input | Expected Output | Reason |
|---|---|---|---|
| Single element | `[5]` | `-1` | No second element exists |
| All identical | `[4, 4, 4]` | `-1` | No distinct second value |
| Two identical + one distinct | `[3, 3, 1]` | `1` | `1` is the only value less than `3` |
| All negative | `[-5, -1, -3]` | `-3` | Works correctly with `float('-inf')` init |
| Two distinct elements | `[2, 9]` | `2` | Straightforward |
| Descending order | `[9, 7, 5, 3]` | `7` | Second update fires on first step |
| Ascending order | `[1, 3, 5, 9]` | `5` | `largest` and `second` both update progressively |

---

## Code

```python
"""
ARR_002 - Second Largest Element in Array
Approach : Single pass with two-variable tracking
Time     : O(n)
Space    : O(1)
"""

from typing import List


def second_largest(nums: List[int]) -> int:
    if len(nums) < 2:
        return -1

    largest = float('-inf')
    second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num < largest and num > second:
            second = num

    return second if second != float('-inf') else -1


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4, 7, 7, 5], 5),
        ([7, 7, 7],          -1),
        ([1],                -1),
        ([-3, -1, -4, -2],   -2),
        ([2, 9],              2),
        ([9, 7, 5, 3],        7),
        ([3, 3, 1],           1),
    ]

    for nums, expected in test_cases:
        result = second_largest(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  Input: {nums}  =>  Output: {result}  (Expected: {expected})")
```

---

## Complexity Summary

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Brute Force (Sorting) | O(n log n + n) | O(n) | Sort copy + backward scan |
| Better (Two Pass) | O(2n) | O(1) | Two separate linear traversals |
| Optimal (Single Pass) | O(n) | O(1) | One traversal, two scalar variables |

---

## Common Mistakes

**1. Initializing `second_largest` to `0` instead of `float('-inf')`**
- Breaks entirely when all values are negative or when the second largest is itself negative
- Always initialize tracking variables to `float('-inf')` for max-finding problems

**2. Not skipping duplicates of `largest`**
- Using `num != largest` in the elif condition silently handles duplicates
- Forgetting this causes `largest` to be returned as `second_largest` when duplicates exist

**3. Using `>=` instead of `>` in the elif condition**
- `elif num >= second` would allow `largest` duplicates to overwrite `second_largest`
- The condition must be `num < largest and num > second` — both bounds are strict

**4. Sorting the original array in-place**
- `nums.sort()` mutates the caller's data; prefer `sorted(nums)` if a copy is needed
- In interview settings, always clarify whether input mutation is acceptable

**5. Returning `second_largest` without checking if it was ever updated**
- If all elements are equal, `second` remains `float('-inf')` — return `-1` in this case
- The guard `return second if second != float('-inf') else -1` handles this correctly

**6. Confusing "second largest value" with "second largest index"**
- The problem asks for the value, not the position
- If position is needed, it requires a separate tracking variable

---

## Revision Trigger

> Two variables, one pass — when `num > largest`, push largest down to second; when `num < largest` and `num > second`, update second directly.

---

*Part of the `strivers-a2z-dsa-python` repository — Arrays / Easy*