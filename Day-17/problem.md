# Day 17: Letter Combinations of a Phone Number

**Difficulty:** Medium  
**Topics:** String, Backtracking, Recursion

---

## Problem Statement

Given a string containing digits from 2–9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (like on telephone buttons) is given. Note that digit '1' does not map to any letters.

---

## Examples

**Example 1:**  
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

markdown
Copy
Edit

**Example 2:**  
Input: digits = ""
Output: []

markdown
Copy
Edit

**Example 3:**  
Input: digits = "2"
Output: ["a","b","c"]

yaml
Copy
Edit

---

## Constraints

- `0 <= digits.length <= 4`  
- `digits[i]` is a digit in the range `['2', '9']`.