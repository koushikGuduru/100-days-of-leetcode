# Day 18: 4Sum

**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Sorting

---

## Problem Statement

Given an array `nums` of `n` integers, return all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`
- `a`, `b`, `c`, and `d` are distinct.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in any order.

---

## Examples

**Example 1:**  
Input: `nums = [1,0,-1,0,-2,2]`, `target = 0`  
Output: `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`

yaml  
Copy  
Edit

**Example 2:**  
Input: `nums = [2,2,2,2,2]`, `target = 8`  
Output: `[[2,2,2,2]]`

yaml  
Copy  
Edit

---

## Constraints

- `1 <= nums.length <= 200`  
- `-10⁹ <= nums[i] <= 10⁹`  
- `-10⁹ <= target <= 10⁹`
