### 📝 Day 11: Container With Most Water — Notes

**Approach:**  
To find the maximum water a container can store between two lines, we need to:

- Use **two pointers**, one starting at the beginning (`left`) and one at the end (`right`) of the array.
- At every step:
  - Calculate the area between the two lines:  
    `area = min(height[left], height[right]) * (right - left)`
  - Keep track of the maximum area found.
  - Move the pointer pointing to the **shorter line**, because moving the taller line can't increase area.

---

**Why Two Pointers?**  
- Brute force (nested loops) gives O(n²) time — too slow.
- Two pointers reduce time to **O(n)** — more efficient.

---

**Example Walkthrough (height = [1,8,6,2,5,4,8,3,7]):**
- Start with lines at index 0 and 8 → area = min(1,7) * (8-0) = 7 * 1 = 7
- Move the shorter line (left++)
- Continue updating the max area
- Max area found = **49** (between heights 8 and 7 at index 1 and 8)

---

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

**Key Insight:**  
The area is limited by the **shorter height**, not the taller one.
