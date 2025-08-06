# Notes - Roman to Integer

**Approach:**

1. Create a dictionary that maps each Roman numeral to its integer value.
2. Iterate through the string from left to right.
3. For each character, check if the current numeral is less than the next one:
   - If yes, subtract it from the result (subtractive notation).
   - If no, add it to the result.

**Key Idea:**
- If the current value is less than the next value, subtract it.
- Otherwise, add it.

**Code:**

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        total = 0

        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total + roman[s[-1]]
