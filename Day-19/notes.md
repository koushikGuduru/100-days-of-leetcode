# Notes – Remove Nth Node From End of List

---

## Approach

This is a classic **two-pointer** problem on linked lists:

1. Use a **dummy node** to simplify edge cases (like removing the head).
2. Initialize two pointers: `fast` and `slow`, both starting at the dummy.
3. Move `fast` ahead by `n + 1` steps.
4. Move both `fast` and `slow` one step at a time until `fast` reaches the end.
5. `slow.next` will be the node to remove — skip it by updating `slow.next = slow.next.next`.

---

## Why Two Pointers Work

- By moving `fast` ahead `n` steps, the gap between `fast` and `slow` ensures that when `fast` hits the end, `slow` is just before the node to delete.
- This avoids needing to count the total length of the list.

---

## Complexity Analysis

- **Time Complexity:** O(sz) — single pass through the list
- **Space Complexity:** O(1) — no extra space used

---

## Edge Cases

- Removing the head node
- List with only one node
- `n` equals the length of the list

---

## Example Flow (head = [1,2,3,4,5], n = 2)

1. Dummy → 1 → 2 → 3 → 4 → 5  
2. Move `fast` ahead 3 steps (n+1)  
3. Move both pointers until `fast` hits null  
4. `slow` is at node 3 → skip node 4  
5. Result: [1,2,3,5]
