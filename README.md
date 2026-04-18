# strivers-a2z-dsa-python

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License: MIT" />
  <img src="https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square" alt="Status" />
  <img src="https://img.shields.io/badge/Sheet-Striver%20A2Z%20DSA-blue?style=flat-square" alt="Striver Sheet" />
  <img src="https://img.shields.io/badge/Focus-Interview%20Preparation-lightgrey?style=flat-square" alt="Focus" />
</p>

A structured Python repository solving problems from **Striver's A2Z DSA Sheet** — organized by topic, written with clean and readable code, and designed to support systematic interview preparation.

---

## About This Repository

This repository is a complete, topic-wise implementation of the [Striver A2Z DSA Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/) in Python. Each solution is written with clarity and correctness as the primary goals — with attention to time and space complexity, edge case handling, and code readability.

The structure is designed to serve as a long-term reference for anyone preparing for technical interviews or building a strong foundation in data structures and algorithms using Python.

---

## About Striver's A2Z DSA Sheet

The **A2Z DSA Sheet** by [Striver (Raj Vikramaditya)](https://takeuforward.org/) is one of the most comprehensive and structured roadmaps for learning Data Structures and Algorithms from scratch to advanced level.

It covers over **450+ problems** across all major DSA topics — ranging from arrays and recursion to graphs, dynamic programming, and tries.

**Sheet Link:** [https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)

---

## Features

- Topic-wise folder organization aligned with Striver's sheet structure
- Clean, well-commented Python solutions with meaningful variable names
- Time and space complexity documented for each solution
- Centralized test suite using `pytest` with JSON-based test case files
- A reusable test runner utility for uniform test execution
- Progress tracker maintained in this README

---

## Folder Structure

```
strivers-a2z-dsa-python/
│
├── arrays/
│   ├── easy/
│   ├── medium/
│   └── hard/
│
├── binary_search/
│
├── bit_manipulation/
│
├── dynamic_programming/
│
├── graphs/
│
├── greedy/
│
├── linked_list/
│
├── recursion/
│
├── stack_queue/
│
├── strings/
│
├── trees/
│
├── tries/
│
├── assets/
│
├── notes/
│
├── testcases/
│   ├── arrays_easy.json
│   ├── binary_search.json
│   └── ...
│
├── tests/
│   └── test_solutions.py
│
├── utils/
│   └── runner.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Folder Explanation

| Folder / File | Description |
|---|---|
| `arrays/` | Array problems split into `easy/`, `medium/`, and `hard/` subdirectories |
| `binary_search/` | Binary search problems — 1D arrays, search on answers, 2D arrays |
| `bit_manipulation/` | Bitwise tricks and interview-level bit manipulation problems |
| `dynamic_programming/` | Complete DP coverage: 1D, 2D, subsequences, strings, stocks, trees |
| `graphs/` | BFS, DFS, shortest path, MST, cycle detection, topological sort |
| `greedy/` | Greedy strategy problems across difficulty levels |
| `linked_list/` | Singly and doubly linked list problems, including medium-hard variants |
| `recursion/` | Pure recursion, subsequence generation, and backtracking problems |
| `stack_queue/` | Stack and queue fundamentals, monotonic stack, expression evaluation |
| `strings/` | String manipulation problems from basic to medium difficulty |
| `trees/` | Binary tree traversals, views, paths, BST, and construction problems |
| `tries/` | Trie data structure concepts and related problems |
| `assets/` | Diagrams, complexity charts, and visual aids for topics |
| `notes/` | Topic-wise revision notes and concept summaries |
| `testcases/` | Centralized JSON files containing input/output pairs per topic |
| `tests/` | `pytest`-based test suite referencing the `testcases/` directory |
| `utils/runner.py` | Shared utility to load JSON test cases and execute solution functions |
| `requirements.txt` | Python dependencies (`pytest`, etc.) |

---

## How to Use

### Prerequisites

- Python 3.10 or higher
- `pip` package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/strivers-a2z-dsa-python.git
cd strivers-a2z-dsa-python

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Running a Solution

Navigate to any topic folder and run the file directly:

```bash
cd arrays/easy
python two_sum.py
```

### Running All Tests

```bash
pytest tests/ -v
```

---

## Example Problem

**Problem:** Two Sum  
**Topic:** Arrays — Easy  
**File:** `arrays/easy/two_sum.py`

```python
"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Given an array of integers `nums` and an integer `target`,
return indices of the two numbers such that they add up to target.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # Output: [0, 1]
    print(two_sum([3, 2, 4], 6))        # Output: [1, 2]
```

---

## Testing

### Framework

This repository uses [`pytest`](https://docs.pytest.org/) as the primary testing framework. All test cases are decoupled from solution logic using a centralized JSON-based test case system.

### Structure

```
testcases/
├── arrays_easy.json
├── binary_search.json
└── graphs.json

tests/
└── test_solutions.py

utils/
└── runner.py
```

### JSON Test Case Format

Each JSON file contains an array of test cases with `input` and `expected` fields:

```json
[
  {
    "description": "Two Sum - basic case",
    "input": { "nums": [2, 7, 11, 15], "target": 9 },
    "expected": [0, 1]
  },
  {
    "description": "Two Sum - repeated element",
    "input": { "nums": [3, 2, 4], "target": 6 },
    "expected": [1, 2]
  }
]
```

### Test Runner Utility

`utils/runner.py` provides a helper to load test cases and bind them to solution functions:

```python
import json
import os

def load_test_cases(filename: str) -> list:
    path = os.path.join(os.path.dirname(__file__), "../testcases", filename)
    with open(path, "r") as f:
        return json.load(f)
```

### Sample Test File

```python
# tests/test_solutions.py

import pytest
from utils.runner import load_test_cases
from arrays.easy.two_sum import two_sum

cases = load_test_cases("arrays_easy.json")

@pytest.mark.parametrize("case", cases)
def test_two_sum(case):
    result = two_sum(**case["input"])
    assert sorted(result) == sorted(case["expected"]), case["description"]
```

### Run Tests

```bash
# Run all tests with verbose output
pytest tests/ -v

# Run tests for a specific topic
pytest tests/test_solutions.py -v -k "two_sum"
```

---

## Notes and Learning

Each solution file follows a consistent documentation pattern:

- **Problem statement** summarized at the top
- **Approach** explained briefly in comments
- **Time and space complexity** noted before the function
- **Edge cases** handled within the logic

> This repository is not just a collection of solutions. It is a study log — intended to build pattern recognition and reinforce problem-solving fundamentals over time.

Key learning principles applied throughout:

- Prefer readability over cleverness
- Choose the optimal approach, but document the brute-force baseline when it adds context
- Revisit problems after intervals to reinforce retention

---

## Visual Assets

> This section is reserved for visual aids such as algorithm animations, complexity comparison charts, and topic mind maps.

Planned additions:

| Asset | Status |
|---|---|
| Array traversal pattern diagram | Planned |
| Binary search decision tree | Planned |
| Graph algorithm flowcharts | Planned |
| DP state transition diagrams | Planned |

Visuals will be placed in a top-level `assets/` folder and linked within individual step README files.

---

## Progress Tracker

| Topic | Folder | Problems Total | Solved | Status |
|---|---|---|---|---|
| Arrays | `arrays/` | 40 | 0 | In Progress |
| Binary Search | `binary_search/` | 32 | 0 | Pending |
| Bit Manipulation | `bit_manipulation/` | 18 | 0 | Pending |
| Dynamic Programming | `dynamic_programming/` | 56 | 0 | Pending |
| Graphs | `graphs/` | 54 | 0 | Pending |
| Greedy | `greedy/` | 16 | 0 | Pending |
| Linked List | `linked_list/` | 31 | 0 | Pending |
| Recursion & Backtracking | `recursion/` | 25 | 0 | Pending |
| Stacks & Queues | `stack_queue/` | 30 | 0 | Pending |
| Strings | `strings/` | 17 | 0 | Pending |
| Trees | `trees/` | 55 | 0 | Pending |
| Tries | `tries/` | 7 | 0 | Pending |
| **Total** | | **381+** | **0** | **In Progress** |

---

## Contribution Guidelines

This repository is primarily a personal learning project, but contributions that improve clarity, fix errors, or add missing test cases are welcome.

### How to Contribute

```bash
# Fork the repository and clone your fork
git clone https://github.com/<your-username>/strivers-a2z-dsa-python.git

# Create a new branch for your change
git checkout -b fix/solution-name

# Make your changes and commit
git commit -m "fix: correct time complexity for two_sum approach"

# Push and open a Pull Request
git push origin fix/solution-name
```

### Contribution Standards

- Follow the existing file naming convention: `snake_case.py`
- Include the problem statement, approach, and complexity in the docstring
- Add or update the corresponding JSON test case for any new solution
- Do not submit solutions copied directly from online sources without understanding

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

In plain terms: you are free to use, modify, and distribute this code for any purpose — personal, academic, or commercial — with no warranty implied. Attribution is appreciated but not required.

See the full [LICENSE](./LICENSE) file for details.

---

## Author

**Abir Barman**  
MCA — VIT Bhopal University  
Areas of Focus: Data Science, Artificial Intelligence & ML, Data Structures & Algorithms, Quantum Computing

<p align="left">
  <a href="https://github.com/<your-username>">
    <img src="https://img.shields.io/badge/GitHub-Profile-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://linkedin.com/in/<your-linkedin>">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" />
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