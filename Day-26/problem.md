# Day 26: Remove Duplicates from Sorted Array

**Difficulty:** Easy  
**Topics:** Array, Two Pointers, In-place Manipulation

---

## Problem Statement

Given a sorted integer array `nums` in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. Keep the relative order of elements the same. Return the number of unique elements, denoted as `k`.

After the function, the first `k` elements of `nums` should be the unique values. The remaining elements beyond `k` are irrelevant.

---

## Examples

**Example 1:**  
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Two unique elements: 1 and 2.

markdown
Copy
Edit

**Example 2:**  
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,,,,,_]
Explanation: Five unique elements found.

yaml
Copy
Edit

---

## Constraints

- `0 <= nums.length <= 3 × 10⁴`
- `-10⁴ <= nums[i] <= 10⁴`
- `nums` is sorted in non-decreasing order.
