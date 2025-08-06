# Notes: Longest Common Prefix

---

## 🔍 Understanding the Problem:

We are given an array of strings. We need to find the longest string prefix that is common to all strings in the array. If there's no common prefix at all, return an empty string.

---

## 🧠 Intuition:

Start with the first string as the assumed common prefix. Compare it with each subsequent string and shrink the prefix from the end until it matches the beginning of the next string. Repeat this process for all strings.

---

## 🧮 Dry Run:

Example:  
Input: `["flower", "flow", "flight"]`  
Initial prefix: `"flower"`

1. Compare with `"flow"` → common: `"flow"`  
2. Compare `"flow"` with `"flight"` → common: `"fl"`

Final output: `"fl"`

---

## ✅ Edge Cases:

- If `strs` is empty → return `""`
- If any string is empty → return `""`
- If no common prefix at all → return `""`

---

## 🛠️ Time and Space Complexity:

- **Time Complexity:** O(S), where S is the sum of all characters in all strings.
- **Space Complexity:** O(1) (in-place prefix trimming)
