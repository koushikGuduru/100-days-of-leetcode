# Day 27: Remove Element

**Difficulty:** Easy  
**Topics:** Array, Two Pointers, In-place Manipulation

---

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place. The order of elements may be changed. After removal, return the number of elements `k` in the modified array that are not equal to `val`.

Elements beyond index `k` are unspecified.

---

## Examples

**Example 1:**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_]
Explanation: Two elements (2,2) remain.

markdown
Copy
Edit

**Example 2:**
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,3,0,4,,,_]

yaml
Copy
Edit

---

## Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`
