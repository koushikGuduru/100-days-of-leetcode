# Notes – Day 16: 3Sum Closest

---

## Approach Overview

1. **Sort** the input array to enable efficient two-pointer technique.
2. Initialize `closest_sum` with a large value (e.g. `infinity`).
3. Iterate through the array, fixing one number at index `i`.
4. For each `i`, use two pointers (`left = i + 1`, `right = end`) to evaluate potential triplets:
   - Calculate current sum: `cur_sum = nums[i] + nums[left] + nums[right]`.
   - Update `closest_sum` if `cur_sum` is closer to `target`.
   - If `cur_sum < target`: increment `left` to increase sum.
   - If `cur_sum > target`: decrement `right` to decrease sum.
   - If `cur_sum == target`: return immediately (perfect match).

---

## Rationale

- Sorting brings similar numbers closer, enabling efficient search with two pointers.
- Checking distances (`abs(cur_sum - target)`) ensures we get the closest sum.
- Two-pointer window shrinks search space to O(n²), scalable up to 500 elements.

---

## Time & Space Complexity

- **Time:** O(n²) — Sorting: O(n log n); For each `i`, a two-pointer scan: O(n)
- **Space:** O(1) — In-place sorting + constant extra space for variables

---

## Edge Cases Considered

- Arrays with only three elements
- Mixed signs, zeroes, etc.
- Guaranteed single solution simplifies result handling

---

## Key Takeaway

Using sorted two-pointer strategy gets us an optimal closest sum efficiently—a great pattern for array-based sum approximations.