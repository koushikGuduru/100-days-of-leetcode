# Notes - Day 3: Longest Substring Without Repeating Characters

## 💡 Key Takeaways:

- Used the **Sliding Window** technique to keep track of a substring without repeating characters.
- Used a **set** to store unique characters in the current window.
- On encountering a duplicate, the left pointer is moved right until the duplicate is removed.

---

## 🔄 Logic Flow:

1. Initialize an empty set `char_set` to track characters.
2. Initialize two pointers `left` and `right` to define the window.
3. For each character at `right`, if it’s already in `char_set`, remove characters from the left side until it's gone.
4. Update the `max_len` at each step.

---

## ⏱️ Time & Space Complexity:

- **Time:** O(n) — each character is visited at most twice.
- **Space:** O(min(n, m)) — where m is the size of the character set (ASCII/Unicode).

---

## ✅ What I Practiced:

- Sliding window technique for strings.
- Efficient substring management.
- Set operations for fast lookup.

