# Notes - Day 1: Two Sum

## 🧠 My Approach

Started with brute-force using two loops, but optimized using a hash map to bring time complexity down to O(n).

- Loop through the list once.
- For each number, calculate its complement (target - num).
- Check if the complement already exists in the map.
- If it does, return the current index and the index of the complement.

## 🔍 What I Learned

- Efficient use of hash maps
- The "store-after-checking" pattern
- A very common pattern in many future problems
