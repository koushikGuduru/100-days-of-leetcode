# Day 16: 3Sum Closest

**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Sorting

---

## Problem Statement

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers.

You may assume that each input has exactly one solution.

---

## Examples

**Example 1:**  
Input: nums = [-1, 2, 1, -4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)

markdown
Copy
Edit

**Example 2:**  
Input: nums = [0, 0, 0], target = 1
Output: 0
Explanation: Closest sum is 0 (0 + 0 + 0 = 0)

yaml
Copy
Edit

---

## Constraints

- `3 <= nums.length <= 500`  
- `-1000 <= nums[i] <= 1000`  
- `-10⁴ <= target <= 10⁴`