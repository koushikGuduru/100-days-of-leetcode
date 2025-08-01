# Day 9 Notes: Palindrome Number

## 🔍 Observation

- A number is a palindrome if it reads the same forward and backward.
- Negative numbers are never palindromes due to the '-' sign.
- A single-digit number is always a palindrome.

---

## ✅ Solution Explanation

- First, check if the number is negative. If so, return `False`.
- Convert the number to a string and compare it with its reverse using slicing (`[::-1]`).

---

## ⏱️ Time and Space Complexity

- **Time Complexity**: O(n), where n is the number of digits in the integer.
- **Space Complexity**: O(n), because we create a string to store the reversed number.

---

## 🧪 Edge Cases

- `x = 0`: Should return `True`
- `x = -121`: Negative → return `False`
- `x = 1001`: Should return `True`

---

## ✨ Alternative (Without converting to string)

- Rebuild half of the number and compare with the other half.
- More efficient, avoids string conversion, but adds complexity.

This solution is clean, simple, and good for interviews.
