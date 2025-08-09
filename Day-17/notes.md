# Notes – Letter Combinations of a Phone Number

---

## Approach

This is a classic **backtracking (DFS)** problem:

1. Map each digit ('2'–'9') to its corresponding letters (e.g., '2' → "abc").  
2. Use a helper function to build combinations recursively:
   - Track current index in the input string.
   - Build the current combination string as you go.
   - If you've processed all digits, add the built string to the result list.

This approach explores all possible letter combinations systematically.

---

## Why Backtracking Works

- The branching factor is small (maximum 4 letters per digit), and the maximum depth is 4 (digits length ≤ 4), making recursion efficient.
- Using backtracking ensures we explore a tree of possibilities and rollback appropriately after each attempt.

---

## Complexity Analysis

- **Time Complexity:** O(4ⁿ) (n = length of digits) — each digit can branch into up to 4 letters. This is manageable since n ≤ 4.
- **Space Complexity:** O(n) for recursion call stack and temporary buffer.

---

## Edge Cases

- Empty input: return an empty list.
- Single digit: just return its mapped letters.

---

## Example Flow (digits = "23")

1. Start with digits = "23", current string = "".  
2. Choose '2' → loop through 'a', 'b', 'c':
   - Pick 'a', move to '3' → loop through 'd', 'e', 'f':
     - "ad", "ae", "af" added to result.
   - Backtrack to prefix "a", pick 'b', then "bd", "be", "bf", etc.
---