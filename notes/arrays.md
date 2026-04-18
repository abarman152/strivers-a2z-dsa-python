# ARR_001 - Largest Element in Array

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Topic-Arrays-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Solved-success?style=flat-square" />
</p>

---

## Problem Statement

Given an array of integers, return the largest element present in the array.

```
Input:  [3, 2, 1, 5, 2]
Output: 5

Input:  [-4, -1, -9, -2]
Output: -1
```

---

## Key Insight

The largest element can be found in a single left-to-right pass by tracking a running maximum — sorting is unnecessary and wastes time.

---

## Approaches

### Brute Force — Sorting

**Explanation:**
Sort the array in ascending or descending order. The largest element will be at the last (or first) index after sorting.

**Why it works:**
Sorting arranges all elements in order, so the maximum is trivially accessible at one end.

**Drawback:**
Sorting does more work than needed. The problem only asks for one value, not a fully ordered array.

| Complexity | Value |
|---|---|
| Time | O(n log n) |
| Space | O(1) if in-place sort, O(n) if not |

```python
def largest_element_brute(nums: list[int]) -> int:
    nums.sort()
    return nums[-1]
```

---

### Optimal Approach — Single Pass Traversal

**Explanation:**
Initialize a variable `max_val` with the first element. Traverse the array once, updating `max_val` whenever a larger element is encountered.

**Step-by-step logic:**
1. Set `max_val = nums[0]`
2. For each element `num` in `nums[1:]`:
   - If `num > max_val`, update `max_val = num`
3. Return `max_val`

**Why it is optimal:**
Each element is visited exactly once. No extra space is used. This is the theoretical minimum for this problem — you must look at every element at least once.

| Complexity | Value |
|---|---|
| Time | O(n) |
| Space | O(1) |

---

## Visualization

```
Input: [3, 2, 1, 5, 2]

Initial  →  max_val = 3

Step 1   →  compare 2  →  2 < 3   →  max_val = 3
Step 2   →  compare 1  →  1 < 3   →  max_val = 3
Step 3   →  compare 5  →  5 > 3   →  max_val = 5
Step 4   →  compare 2  →  2 < 5   →  max_val = 5

Output   →  5
```

```
Input: [-4, -1, -9, -2]

Initial  →  max_val = -4

Step 1   →  compare -1  →  -1 > -4  →  max_val = -1
Step 2   →  compare -9  →  -9 < -1  →  max_val = -1
Step 3   →  compare -2  →  -2 < -1  →  max_val = -1

Output   →  -1
```

---

## Pattern Recognition

**Tags:** `#array` `#traversal` `#max_tracking` `#single_pass` `#greedy`

**When to use this pattern:**
- Finding a single aggregate value (max, min, sum, product) over an array
- No need for the array to be ordered — just need one pass
- Any problem where you track a "running best" across elements

**Related problems:**
- Second Largest Element in Array
- Minimum Element in Array
- Find the element with maximum frequency
- Maximum subarray sum (Kadane's Algorithm — same running-best principle)

---

## Edge Cases

| Case | Input | Expected Output | Handled By |
|---|---|---|---|
| Single element | `[7]` | `7` | `max_val` initialized to `nums[0]`, loop does not execute |
| All negative numbers | `[-3, -1, -4, -2]` | `-1` | Initializing to `nums[0]` (not `0`) ensures correctness |
| All duplicates | `[5, 5, 5, 5]` | `5` | No update occurs after init; returns correctly |
| Already sorted ascending | `[1, 2, 3, 4, 5]` | `5` | Max updated at every step; final value is last element |
| Already sorted descending | `[5, 4, 3, 2, 1]` | `5` | Max set at init; no updates needed |

---

## Code

```python
"""
ARR_001 - Largest Element in Array
Approach : Single pass traversal
Time     : O(n)
Space    : O(1)
"""

from typing import List


def largest_element(nums: List[int]) -> int:
    max_val = nums[0]

    for num in nums[1:]:
        if num > max_val:
            max_val = num

    return max_val


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 5, 2], 5),
        ([-4, -1, -9, -2], -1),
        ([7], 7),
        ([5, 5, 5, 5], 5),
    ]

    for nums, expected in test_cases:
        result = largest_element(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  Input: {nums}  =>  Output: {result}  (Expected: {expected})")
```

---

## Revision Trigger

> Find max in array — single pass with running max, never sort.

---

## Common Mistakes

**1. Initializing `max_val` to `0` instead of `nums[0]`**
- Fails entirely when all elements are negative
- Always initialize to the first element of the array, not a hardcoded value

**2. Using sort when only the max is needed**
- Sorting is O(n log n) — it solves a harder problem (full ordering) than required
- Any time you catch yourself sorting just to access one end, reconsider

**3. Returning index instead of value**
- The problem asks for the element itself, not its position
- If the position is needed, track `max_idx` separately

**4. Not handling single-element arrays**
- The loop `nums[1:]` handles this gracefully — it simply does not execute
- Avoid writing `range(1, len(nums))` with manual index access without confirming the array is non-empty

**5. Mutating the input array**
- The brute-force sorting approach modifies the original array in-place
- If the caller's array must be preserved, sort a copy: `sorted(nums)[-1]`

---

## Complexity Summary

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Brute Force (Sorting) | O(n log n) | O(1) / O(n) | Depends on sort implementation |
| Optimal (Single Pass) | O(n) | O(1) | Theoretical minimum for this problem |

---

*Part of the `strivers-a2z-dsa-python` repository — Arrays / Easy*