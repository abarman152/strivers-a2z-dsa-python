# strivers-a2z-dsa-python

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License: MIT" />
  <img src="https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square" alt="Status" />
  <img src="https://img.shields.io/badge/Sheet-Striver%20A2Z%20DSA-blue?style=flat-square" alt="Striver Sheet" />
  <img src="https://img.shields.io/badge/Focus-Interview%20Preparation-lightgrey?style=flat-square" alt="Focus" />
</p>

A structured Python repository solving problems from **Striver's A2Z DSA Sheet** — organized by topic with ID-based naming, marker-based testing, and a parallel notes system designed for systematic interview preparation.

---

## About This Repository

This repository implements the [Striver A2Z DSA Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/) in Python. It is not a plain collection of solutions — it is a learning system with three distinct concerns: solution code, test validation, and structured notes.

Each component serves a specific purpose. The code files contain only the optimal solution. The test suite validates correctness through pytest markers. The notes directory captures the thinking process, patterns, and brute-to-optimal progression that the code itself does not show.

---

## About Striver's A2Z DSA Sheet

The **A2Z DSA Sheet** by [Striver (Raj Vikramaditya)](https://takeuforward.org/) is one of the most comprehensive structured roadmaps for learning Data Structures and Algorithms from scratch to advanced level. It covers **450+ problems** across all major DSA topics.

**Sheet Link:** [https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)

---

## System Design Philosophy

### ID-Based Naming

Every problem file is prefixed with a topic code and a zero-padded numeric ID:

```
arr_001_largest_element.py
arr_002_second_largest.py
```

This enforces:
- **Ordered progression** — problems are tackled in sequence, not arbitrarily
- **Unambiguous tracking** — each problem has a permanent identity that does not shift when files are added
- **Pattern mapping** — IDs allow notes and tests to reference the same problem without relying on inconsistent names

### Optimal-Only Code

Each `.py` file contains one implementation: the optimal solution. The brute-force and intermediate approaches are documented in the corresponding notes file, not in the solution code. This keeps the code clean, readable, and production-quality — reflecting how a senior engineer would write it after understanding the problem fully.

### Separation of Concerns

| Component | Purpose |
|---|---|
| `.py` solution files | Clean optimal implementation, complexity analysis, edge case handling |
| `tests/` | Correctness validation via pytest markers |
| `notes/` | Brute-to-optimal thinking, pattern recognition, interview context |

These three components are intentionally decoupled. Reading a solution file should not require scrolling past multiple approaches. Running tests should not require understanding the notes. Studying patterns should not be mixed with implementation detail.

---

## Folder Structure

```
strivers-a2z-dsa-python/
│
├── arrays/
│   ├── easy/
│   │   ├── arr_001_largest_element.py
│   │   ├── arr_002_second_largest.py
│   │   └── ...
│   ├── medium/
│   └── hard/
│
├── binary_search/
├── bit_manipulation/
├── dynamic_programming/
├── graphs/
├── greedy/
├── linked_list/
├── recursion/
├── stack_queue/
├── strings/
├── trees/
├── tries/
│
├── notes/
│   ├── arrays_easy.md
│   ├── binary_search.md
│   └── ...
│
├── tests/
│   └── test_arrays_easy.py
│
├── assets/
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Naming Convention

All solution files follow this pattern:

```
<topic_prefix>_<id>_<problem_name>.py
```

| Segment | Description |
|---|---|
| `topic_prefix` | Short lowercase code for the topic (`arr`, `bs`, `ll`, `dp`, etc.) |
| `id` | Zero-padded three-digit sequence number (`001`, `002`, ...) |
| `problem_name` | Snake-case problem description |

**Examples:**

| File | Topic | Problem |
|---|---|---|
| `arr_001_largest_element.py` | Arrays | Largest Element in Array |
| `arr_002_second_largest.py` | Arrays | Second Largest Element |
| `bs_001_binary_search.py` | Binary Search | Standard Binary Search |
| `ll_001_reverse_linked_list.py` | Linked List | Reverse a Linked List |

---

## File Structure Per Problem

Each solution file contains:

```python
"""
Problem: Largest Element in Array
ID: ARR_001
Link: https://leetcode.com/problems/...
Difficulty: Easy

Find the largest element in an unsorted array.

Intuition:
    A single linear scan suffices — track the running maximum.

Approach:
    Iterate through the array, updating max_val when a larger element is found.

Time Complexity: O(n)
Space Complexity: O(1)

Edge Cases:
    - Single element array
    - All elements equal
    - Negative numbers
"""

from typing import List


def largest_element(nums: List[int]) -> int:
    max_val = nums[0]
    for num in nums[1:]:
        if num > max_val:
            max_val = num
    return max_val


if __name__ == "__main__":
    print(largest_element([3, 1, 4, 1, 5, 9, 2, 6]))  # 9
```

No alternative approaches appear in the `.py` file. Brute-force and intermediate solutions are in the corresponding notes file.

---

## Testing Strategy

### Framework

Tests use [`pytest`](https://docs.pytest.org/) with **marker-based execution**. Each test function is tagged with a marker matching the problem ID, allowing isolated or bulk test runs without any JSON fixtures or external test runners.

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run tests for a specific problem
pytest -m largest_element -v
pytest -m second_largest -v

# Run all array easy tests
pytest tests/test_arrays_easy.py -v
```

### Test File Structure

```python
# tests/test_arrays_easy.py

import pytest
from arrays.easy.arr_001_largest_element import largest_element
from arrays.easy.arr_002_second_largest import second_largest


@pytest.mark.largest_element
class TestLargestElement:
    def test_basic(self):
        assert largest_element([3, 1, 4, 1, 5, 9]) == 9

    def test_single_element(self):
        assert largest_element([7]) == 7

    def test_all_equal(self):
        assert largest_element([4, 4, 4]) == 4

    def test_negative_numbers(self):
        assert largest_element([-3, -1, -7]) == -1


@pytest.mark.second_largest
class TestSecondLargest:
    def test_basic(self):
        assert second_largest([3, 1, 4, 1, 5, 9]) == 5

    def test_two_elements(self):
        assert second_largest([2, 1]) == 1
```

### Marker Registration

Markers are declared in `pytest.ini` or `pyproject.toml`:

```ini
[pytest]
markers =
    largest_element: ARR_001 - Largest Element
    second_largest: ARR_002 - Second Largest
```

---

## Notes System

Each topic has a corresponding Markdown notes file in `notes/`. Notes are structured to support both learning and revision, not just documentation.

### Notes File Structure

```markdown
# Arrays — Easy

## ARR_001 — Largest Element

**Pattern:** Linear Scan / Running Maximum

**Brute Force:** Sort the array and return the last element. O(n log n).

**Better:** Not applicable for this problem.

**Optimal:** Single pass with a running maximum. O(n) time, O(1) space.

**Key Insight:** No sorting needed. One traversal is sufficient.

**Interview Notes:**
- Always ask: can the array be empty? Handle that at the boundary.
- Follow-up: find the k-th largest — leads into heap or quickselect.

---

## ARR_002 — Second Largest

**Pattern:** Linear Scan / Two-Variable Tracking

**Brute Force:** Sort descending, return index 1 (handle duplicates). O(n log n).

**Optimal:** Track `max_val` and `second_max` in a single pass. O(n) time, O(1) space.

**Key Insight:** Update `second_max` only when `num < max_val` and `num > second_max`.

**Interview Notes:**
- Edge case: all elements equal — second largest does not exist.
- Follow-up: second largest in a BST — different approach entirely.
```

### Notes Principles

- Brute-to-optimal progression is captured here, not in code
- Each entry is tagged with a **pattern** for cross-problem recognition
- Interview follow-ups and edge cases are noted explicitly
- Notes are meant for active revision, not passive reading

---

## Learning Workflow

1. **Read the problem** — open the `.py` file, read the docstring
2. **Study the notes** — understand the brute-to-optimal thinking in `notes/`
3. **Read the solution** — study the optimal implementation
4. **Run the tests** — validate understanding with `pytest -m <marker>`
5. **Revisit periodically** — use the notes for spaced repetition

---

## Setup

### Prerequisites

- Python 3.10 or higher
- `pip` package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/abarman152/strivers-a2z-dsa-python.git
cd strivers-a2z-dsa-python

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### Running a Solution Directly

```bash
python arrays/easy/arr_001_largest_element.py
```

---

## Progress Tracker

| Topic | Prefix | Total | Solved | Status |
|---|---|---|---|---|
| Arrays | `arr` | 40 | 0 | In Progress |
| Binary Search | `bs` | 32 | 0 | Pending |
| Bit Manipulation | `bit` | 18 | 0 | Pending |
| Dynamic Programming | `dp` | 56 | 0 | Pending |
| Graphs | `gr` | 54 | 0 | Pending |
| Greedy | `grd` | 16 | 0 | Pending |
| Linked List | `ll` | 31 | 0 | Pending |
| Recursion & Backtracking | `rec` | 25 | 0 | Pending |
| Stacks & Queues | `sq` | 30 | 0 | Pending |
| Strings | `str` | 17 | 0 | Pending |
| Trees | `tr` | 55 | 0 | Pending |
| Tries | `trie` | 7 | 0 | Pending |
| **Total** | | **381+** | **0** | **In Progress** |

---

## Contribution Guidelines

This is a personal learning project. Contributions that fix errors, improve clarity, or add missing test cases are welcome.

### Standards

- Follow the naming convention: `<prefix>_<id>_<problem_name>.py`
- Solution files contain only the optimal approach
- Include problem statement, intuition, approach, and complexity in the docstring
- Add corresponding pytest marker and test class for any new solution
- Update the notes file for the relevant topic

### Workflow

```bash
git clone https://github.com/abarman152/strivers-a2z-dsa-python.git
git checkout -b fix/arr-001-edge-case
git commit -m "fix: handle single-element input in arr_001_largest_element"
git push origin fix/arr-001-edge-case
```

---

## License

This project is distributed under the **MIT License**.

```
MIT License

Copyright (c) 2024 Abir Barman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

See the full [LICENSE](./LICENSE) file for details.

---

## Author

**Abir Barman**
MCA — VIT Bhopal University
Areas of Focus: Data Structures & Algorithms, Data Science, Artificial Intelligence & ML, Quantum Computing

<p align="left">
  <a href="https://github.com/abarman152">
    <img src="https://img.shields.io/badge/GitHub-abarman152-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Built%20for-Interview%20Preparation-lightgrey?style=flat-square" />
  &nbsp;
  <img src="https://img.shields.io/badge/Language-Python%203.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/Sheet-Striver%20A2Z-blue?style=flat-square" />
</p>
