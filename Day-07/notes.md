# Notes - Day 7: Reverse Integer

## ✅ Key Observations:
- If the integer is negative, we must preserve the sign after reversing.
- Removing leading zeros from the reversed number is handled automatically when converting strings to int.
- Overflow handling is necessary because the result must lie within 32-bit signed integer bounds: `[-2^31, 2^31 - 1]`.

## 🔍 Steps:
1. Store the sign of `x` and work with its absolute value.
2. Convert the number to a string and reverse it using slicing (`[::-1]`).
3. Convert it back to an integer and reapply the original sign.
4. Check for overflow — if it's outside the range, return `0`.

## ⛔ Edge Cases:
- Input like `1534236469` might overflow after reversal.
- Single-digit inputs or trailing zeros need not be handled manually — converting back to int handles it cleanly.
- Python's `int()` handles leading zeroes correctly, so no special trimming needed.

## 📌 Note:
- Python's int type supports arbitrarily large integers, but for LeetCode, we enforce 32-bit range manually.
