# Day 20: Valid Parentheses

**Difficulty:** Easy  
**Topics:** Stack, String

---

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Every closing bracket has a corresponding opening bracket of the same type.

---

## Examples

**Example 1:**  
Input: `s = "()"`  
Output: `true`

yaml  
Copy  
Edit

**Example 2:**  
Input: `s = "()[]{}"`  
Output: `true`

yaml  
Copy  
Edit

**Example 3:**  
Input: `s = "(]"`  
Output: `false`

yaml  
Copy  
Edit

---

## Constraints

- `1 <= s.length <= 10⁴`  
- `s` consists of parentheses only