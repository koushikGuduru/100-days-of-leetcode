## Approach:

We solve this by expanding around possible centers.

- Each character and each pair of adjacent characters is treated as a possible center.
- For each center, expand as far as the characters match on both sides.
- Keep track of the longest expansion found.

### Why Expand Around Center?
- It avoids checking every substring.
- Efficient: O(n^2) time, O(1) space.

### Edge Cases:
- Empty string: return ""
- Entire string is a palindrome

### Complexity:
- Time: O(n^2)
- Space: O(1)
