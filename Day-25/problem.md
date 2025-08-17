# Day 25: Reverse Nodes in k-Group

**Difficulty:** Hard  
**Topics:** Linked List, Recursion, Iteration, Pointer Manipulation

---

## Problem Statement

Given the head of a linked list and an integer `k`, reverse the nodes of the list `k` at a time and return the modified list.  
- `k` is a positive integer and ≤ the length of the list.  
- If the number of nodes is not a multiple of `k`, the remaining nodes at the end should remain as-is.  
- You must not alter node values—only the node links should change.

---

## Examples

**Example 1:**  
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]


**Example 2:**  


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


**Example 3:**  


Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]


---

## Constraints

- The number of nodes is in the range `[1, 5000]`  
- `0 <= Node.val <= 1000`  
- `1 <= k <= size of the list`