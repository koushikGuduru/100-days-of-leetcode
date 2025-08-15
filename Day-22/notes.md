# Day 22 Notes: Generate Parentheses

---

## Approach Overview

Use **backtracking** to build valid parentheses combinations step by step:

1. Maintain a `path` list to build the current sequence.
2. Track two counters: `open_count` and `close_count`—how many "(" and ")" have been used.
3. The recursive function (`backtrack`) logic:
   - If `open_count < n`, add `"("`, recurse, then backtrack.
   - If `close_count < open_count`, add `")"`, recurse, then backtrack.
4. When `len(path) == 2 * n`, a valid sequence is complete—add it to the result list.

---

## Why This Works

- Ensures **well-formedness** by never adding `")"` unless there's a matching `"("` before it.
- Guaranteed termination because each recursion step increases the total parentheses count.
- Recursion depth and branch factor remain manageable (`n` ≤ 8).

---

## Time and Space Complexity

- **Time Complexity:** O(Catalan(n)) ≈ O(4ⁿ / √n), due to the number of valid parentheses combinations (Catalan numbers).
- **Space Complexity:** O(n) for recursion depth and the path list.

---

## Key Takeaways

- Backtracking is ideal for combinatorial generation with constraints.
- Maintaining counters and pruning invalid paths keeps the solution efficient.
- Often, constructing valid sequences directly is better than generating all and filtering.