# Day 27 Notes: Remove Element

---

## Approach

Use the **two-pointer** technique:

- **Read pointer (`i`)** traverses the entire array.
- **Write pointer (`k`)** tracks the position to place the next valid value (one that isn't `val`).

For every `i`:
- If `nums[i]` is not `val`, copy it to `nums[k]` and increment `k`.

Return `k` as the count of elements not equal to `val`.

---

## Complexity Analysis

- **Time Complexity:** O(n) — single pass through the array.
- **Space Complexity:** O(1) — in-place operation using constant extra space.

---

## Key Points

- Array order can change, but unique elements remain in the first `k` positions.
- Simple and efficient in-place removal.
