# Notes – 4Sum

---

## Approach

This problem is best solved using a **two-pointer technique** after sorting the array:

1. **Sort the array** to make it easier to skip duplicates and use two pointers efficiently.
2. **Fix the first two elements** using nested loops.
3. For the remaining two elements, use **left and right pointers** to find pairs that sum to the required value.
4. **Skip duplicates** at each level to ensure only unique quadruplets are added to the result.

This approach avoids brute-force enumeration of all quadruplets and leverages sorted order for efficiency.

---

## Why Two Pointers Work

- After fixing two numbers, the remaining target becomes a 2Sum problem.
- Sorting allows us to move pointers intelligently:
  - If the sum is too small, move `left` forward.
  - If the sum is too large, move `right` backward.
- This reduces the time complexity significantly compared to checking all combinations.

---

## Complexity Analysis

- **Time Complexity:** O(n³)  
  - Outer two loops: O(n²)
  - Inner two-pointer scan: O(n)
- **Space Complexity:** O(1) (excluding output list)

---

## Edge Cases

- Array with fewer than 4 elements: return empty list.
- Multiple duplicates: ensure results are unique by skipping repeated values.
- Large integers: handle potential overflow (Python handles big integers natively).

---

## Example Flow (nums = [1,0,-1,0,-2,2], target = 0)

1. Sort: [-2, -1, 0, 0, 1, 2]
2. Fix -2 and -1 → look for 3 using two pointers → find [−2,−1,1,2]
3. Fix -2 and 0 → look for 2 → find [−2,0,0,2]
4. Fix -1 and 0 → look for 1 → find [−1,0,0,1]
5. Skip duplicates and continue scanning
