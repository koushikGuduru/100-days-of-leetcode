# Notes – Valid Parentheses

---

## Approach

This is a classic **stack-based** problem:

1. Use a stack to track opening brackets.
2. For each character in the string:
   - If it's an opening bracket, push it onto the stack.
   - If it's a closing bracket, check if the stack is not empty and the top matches the corresponding opening bracket.
   - If not, return `False`.
3. After processing all characters, the stack should be empty for the string to be valid.

---

## Why Stack Works

- Brackets must be closed in the reverse order of opening.
- A stack naturally supports Last-In-First-Out (LIFO) behavior, which matches the nesting structure of valid parentheses.

---

## Complexity Analysis

- **Time Complexity:** O(n) — one pass through the string
- **Space Complexity:** O(n) — in worst case, all characters are opening brackets

---

## Edge Cases

- Empty string: valid by definition
- Mismatched pairs: e.g., `"(]"`, `"([)]"`
- Extra closing brackets: e.g., `"())"`

---

## Example Flow (s = "{[()]}")
1. Push `{`, `[`, `(` onto stack  
2. Match `)` with `(` → pop  
3. Match `]` with `[` → pop  
4. Match `}` with `{` → pop  
5. Stack is empty → valid
