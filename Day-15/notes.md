# Day 15: Notes on 3Sum

## 🔍 Intuition

The brute-force approach would involve three nested loops, leading to O(n³) time complexity, which is inefficient for large arrays.  
Instead, we use sorting and a two-pointer strategy to reduce time complexity.

---

## 💡 Approach

1. Sort the array.
2. Loop through the array, fixing one element.
3. Use two pointers (`left` and `right`) to find the other two elements such that their sum equals `-nums[i]`.
4. Skip duplicates to ensure unique triplets.

---

## 🧠 Key Concepts

- Sorting simplifies the duplicate handling and makes two-pointer approach feasible.
- Use `while` loops inside to skip over duplicate numbers.
- Be careful with edge cases like:
  - All zeroes
  - No valid triplets
  - Multiple duplicates

---

## 🕒 Time Complexity

- Sorting: O(n log n)
- Two-pointer scan: O(n²)

Total: **O(n²)** time complexity, which is efficient for `n ≤ 3000`.

---

## ✅ Best Practices

- Always check for duplicates when the problem requires *unique* combinations.
- Optimize nested loops with sorted arrays and two-pointer strategy when possible.

---

## 📌 Common Pitfalls

- Forgetting to skip duplicate values.
- Not handling edge cases like `[0, 0, 0, 0]`.
- Incorrectly managing pointer increments/decrements.
