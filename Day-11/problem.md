### 11. Container With Most Water

**Difficulty**: Medium  
**Topics**: Array, Two Pointers, Greedy

You are given an integer array `height` of length `n`. There are `n` vertical lines such that the endpoints of the `iᵗʰ` line are `(i, 0)` and `(i, height[i])`.

Find two lines that, together with the x-axis, form a container that holds the most water.

Return the **maximum amount of water** a container can store.

**Note**: The container cannot be slanted.

---

**Example 1:**

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines form a container with the max area of 49.


**Example 2:**

Input: height = [1,1]
Output: 1

#### Constraints:

- `n == height.length`
- `2 <= n <= 10⁵`
- `0 <= height[i] <= 10⁴`