# Notes: String to Integer (atoi)

---

## Key Ideas:

- Skipping whitespace is necessary to avoid misreading input.
- Sign handling must occur before digit conversion.
- Stop reading at the first non-digit character.
- Clamp the result within `[−2³¹, 2³¹ − 1]`.

---

## What I Learned:

✅ How to simulate a simple state machine parser manually  
✅ Importance of step-wise parsing in real-world string processing  
✅ Handling edge cases like empty strings, signs, and overflow  

---

## Time & Space Complexity:

- **Time Complexity:** O(n), where n is the length of the string
- **Space Complexity:** O(1), constant extra space

---

## Tips:

- Watch for inputs like `"  +00123abc"` — valid parsing stops at first non-digit
- Carefully check overflow/underflow before returning

