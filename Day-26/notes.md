# Day 26 Notes: Remove Duplicates from Sorted Array

---

## Approach

Since the array is sorted, duplicates appear consecutively. Use the **two-pointer** technique:

- **Fast pointer (`i`)** traverses the array.
- **Slow pointer (`k`)** tracks the next position for a unique value.

Iterate from `i = 1` to end:
- If `nums[i]` ≠ `nums[i-1]`, it's unique:
  - Assign `nums[k] = nums[i]`
  - Increment `k`
  
At the end, `k` equals the count of unique elements. The array is modified in-place.

---

## Complexity

- **Time Complexity:** O(n) — one pass through the array.
- **Space Complexity:** O(1) — in-place solution with constant extra space.

---

## Key Insights

- Sorting ensures duplicates are adjacent.
- Fast-slow pointer technique keeps shifting uniques to the front.
- Solution adheres to in-place requirement and runs in linear time.
