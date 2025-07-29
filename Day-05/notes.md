## Notes: Longest Palindromic Substring

### ✅ Approach:
We expand around each character (center) to check for the longest palindromic substring.  
There are two types of centers:
- Odd-length palindromes: one center (i)
- Even-length palindromes: two centers (i, i+1)

### ✅ Steps:
1. Initialize `start` and `end` pointers.
2. For each character, expand outward while characters on both sides are equal.
3. Track the maximum length and update `start` and `end`.

### ✅ Time Complexity:
- O(n^2) — we check each possible center and expand.
- O(1) space — we don't use extra space apart from pointers.

### 🧠 Tips:
- Palindromes mirror around a center.
- Use helper function `expandAroundCenter` for clean logic.
