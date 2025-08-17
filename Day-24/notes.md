# Day 24 Notes: Swap Nodes in Pairs

---

## Problem Overview

We need to swap each adjacent pair of nodes in a linked list **by changing links**, not just node values.

---

## Approach: Iterative with Dummy & Pointers

1. Create a `dummy` node before the head for uniform handling (especially head swaps).
2. Use `prev` (initially at `dummy`) and `curr` (initially at `head`).
3. Loop while there are at least two nodes (`curr` and `curr.next`):
   - Identify `first = curr` and `second = curr.next`
   - Rewire pointers to swap the pair:
     - `prev.next = second`
     - `first.next = second.next`
     - `second.next = first`
   - Move pointers:
     - `prev = first`
     - `curr = first.next`
4. Return `dummy.next`, the new head.

---

## Time & Space Complexity

- **Time Complexity:** O(n) — each node is visited once.
- **Space Complexity:** O(1) — constant extra space, only pointers used.

---

## Edge Cases Covered

- Empty list → returns None.
- Single-node list → returns head as-is.
- Works correctly with even or odd numbers of nodes.

---

## Tip

Using a dummy node simplifies edge cases (like swapping at the head) without special conditions.
