# Day 8: String to Integer (atoi)

**LeetCode Problem:** https://leetcode.com/problems/string-to-integer-atoi/  
**Difficulty:** Medium  
**Topics:** String, Parsing

---

## Problem Statement

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

### Steps:

1. **Whitespace**: Ignore leading whitespace.
2. **Signedness**: Check for '+' or '-' and determine the sign.
3. **Conversion**: Convert digits into an integer until a non-digit is encountered.
4. **Rounding**: Clamp the result within the 32-bit signed integer range: `[-2³¹, 2³¹ - 1]`.

---

## Examples

**Input:** `"42"`  
**Output:** `42`

**Input:** `"   -042"`  
**Output:** `-42`

**Input:** `"1337c0d3"`  
**Output:** `1337`

**Input:** `"0-1"`  
**Output:** `0`

**Input:** `"words and 987"`  
**Output:** `0`

---

## Constraints

- `0 <= s.length <= 200`
- `s` consists of English letters (upper/lowercase), digits, whitespace, `+`, `-`, and `.`

