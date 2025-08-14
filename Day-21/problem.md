# Day 21: Merge Two Sorted Lists

**Difficulty:** Easy  
**Topics:** Linked Lists, Recursion, Iteration

---

## Problem Statement

You are given the heads of two sorted linked lists, `list1` and `list2`.

Merge the two lists in a strictly sorted manner. The merged list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

---

## Examples

**Example 1:**
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]

markdown
Copy
Edit

**Example 2:**
Input: list1 = [], list2 = []
Output: []

markdown
Copy
Edit

**Example 3:**
Input: list1 = [], list2 = [0]
Output: [0]

yaml
Copy
Edit

---

## Constraints

- The number of nodes in both lists is in the range `[0, 50]`
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order
