# Day 23 Notes: Merge K Sorted Lists

---

## Approach Overview

We use a **min-heap (priority queue)** to efficiently pull the smallest current node across all lists:

1. Initialize the heap with the head of each non-empty list.
2. Pop the smallest `(value, index, node)` from the heap.
3. Attach `node` to the merged list tail.
4. If `node.next` exists, push it into the heap.
5. Continue until the heap is empty.

This ensures merging in **ascending order**, leveraging the already-sorted nature of lists.

---

## Complexity Analysis

- **Time Complexity**: O(N log k), where:
  - N = total nodes across all lists
  - k = number of lists
  Each `heapq` operation is O(log k), done once per node.

- **Space Complexity**: O(k), the heap size is at most `k`.

---

## Edge Cases Handled

- Empty list of lists → return `None`
- Some lists being empty
- Duplicates and negative values handled implicitly

---

## Alternative Approach

**Divide & Conquer**: Repeatedly merge pairs of lists. Achieves O(N log k) time too, but heap method is simpler to code and understand.