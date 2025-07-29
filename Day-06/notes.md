## Notes: Day 6 - Zigzag Conversion

### 🔍 Problem Summary:
We are given a string `s` and a number of rows `numRows`. We need to rearrange the characters of the string in a zigzag (diagonal + vertical) pattern and then read the characters row by row to produce the final string.

---

### 🧠 Key Observations:
- The pattern moves **downward** through the rows and then **diagonally upward**, repeating this until the string ends.
- If `numRows == 1` or `numRows >= len(s)`, the zigzag pattern would be the same as the original string.
- We can simulate the process by appending characters to the correct row in each step.

---

### 💡 Approach:
1. Create a list of empty strings to represent each row.
2. Use a variable `current_row` to keep track of the current row being filled.
3. Use a `direction` flag to control whether we are going **down** or **up** the rows.
4. Iterate through each character in `s`, placing it in the correct row based on the current direction.
5. At the end, concatenate all rows to get the final result.

---

### ✅ Edge Cases:
- If `numRows == 1`, return the original string.
- Works for both short and long strings (up to 1000 characters).

---

### 📈 Time & Space Complexity:
- **Time Complexity:** O(n), where n is the length of the input string.
- **Space Complexity:** O(n), for storing the characters in row-wise format.

---
