# Day 25 Notes: Reverse Nodes in k-Group

---

## Approach Overview

We reverse the list in fixed groups of `k` using pointer manipulation and a dummy node:

1. Use a dummy node to simplify head handling (`dummy.next = head`).
2. `group_prev` marks the node before the current group.
3. Check if there are at least `k` nodes ahead; if not, exit and return list as-is.
4. Reverse the group:
   - Use pointers `prev` and `curr`.
   - Reverse the nodes up to the node after the group (`group_next`).
5. Reconnect the reversed segment:
   - Link `group_prev.next` to the new head (`kth`).
   - Advance `group_prev` to the tail of the reversed group (previous head).

---

## Complexity Analysis

- **Time Complexity:** O(n), each node is visited and reversed at most once.
- **Space Complexity:** O(1), only pointers are used — no extra lists or recursion depth.

---

## Key Insights

- A dummy node helps avoid edge-case logic when reversing at the head.
- Prechecking group length ensures safe reversal without needing lookahead during loop.
- Reconnecting the segments correctly preserves list integrity with no new nodes required.

---

## Edge Cases Covered

- `k = 1` (list remains the same).
- List length not multiple of `k` (tail left in place).
- Entire list reversed when `k` equals list length.
