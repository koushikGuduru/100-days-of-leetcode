# Notes: Regular Expression Matching

## Key Concepts

- Dynamic Programming is used to handle overlapping subproblems.
- `dp[i][j]` represents whether `s[0...i-1]` matches `p[0...j-1]`.
- `.` matches any character.
- `*` allows for 0 or more of the preceding character.

## Important Cases

- `a*` can match "", "a", "aa", ...
- `.*` can match any sequence
- Be careful with empty string cases (`dp[0][j]`).

## Logic

1. Initialize `dp[0][0] = True` since empty string matches empty pattern.
2. Use nested loops to fill in the `dp` table.
3. For '*', check two scenarios:
   - Ignore previous character + '*': `dp[i][j-2]`
   - Match multiple of previous character: check if `s[i-1] == p[j-2]` or `p[j-2] == '.'`

## Time Complexity

- O(m * n), where `m = len(s)`, `n = len(p)`

## Space Complexity

- O(m * n), for the DP table
