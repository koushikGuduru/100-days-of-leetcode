# Day 23: Merge K Sorted Lists

**Difficulty:** Hard  
**Topics:** Linked List, Heap, Divide & Conquer

---

## Problem Statement

You are given an array of `k` linked lists, each sorted in ascending order. Merge all the linked lists into one sorted linked list and return it.

---

## Examples

**Example 1:**  


Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]


**Example 2:**  


Input: lists = []
Output: []


**Example 3:**  


Input: lists = [[]]
Output: []


---

## Constraints

- `k == lists.length`  
- `0 <= k <= 10⁴`  
- `0 <= lists[i].length <= 500`  
- `-10⁴ <= lists[i][j] <= 10⁴`  
- `lists[i]` is sorted in ascending order.  
- The sum of all `lists[i].length` won’t exceed 10⁴.