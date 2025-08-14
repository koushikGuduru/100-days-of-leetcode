# Notes – Day 21: Merge Two Sorted Lists

---

## Approach

We can merge two sorted linked lists into one sorted list using a **dummy node**:

1. Create a `dummy` node and use a `tail` pointer to build the result list.
2. Compare the heads of both input lists (`p1`, `p2`):
   - Attach the smaller node to `tail.next`
   - Move that pointer (p1 or p2) forward
   - Advance `tail`
3. When one list is exhausted, attach the remaining nodes from the other list.

---

## Why This Works

Because both input lists are sorted:
- This algorithm ensures the merged list remains sorted.
- The dummy node avoids edge-case handling when starting the new list.

---

## Complexity

- **Time Complexity:** O(n + m), where n and m are the lengths of the two lists.
- **Space Complexity:** O(1), since we reuse existing nodes and only adjust pointers.

---

## Edge Cases

- One or both input lists are empty → handled by attaching the non-empty list directly
- Identical values across lists → still works as `<=` logic handles order
