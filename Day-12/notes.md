### Notes: Integer to Roman

Approach:
- Use two parallel arrays:
  - `val`: list of integer values (sorted descending)
  - `syms`: corresponding Roman numeral symbols
- For each value, subtract as many times as possible and append the Roman symbol.
- Continue until the number reduces to 0.

Time Complexity: O(1) — because the range of input is bounded (1 to 3999)  
Space Complexity: O(1)

Key Takeaways:
- Subtractive forms are essential for compact Roman representation.
- Roman numerals are based on decimal positional values — each digit position is treated separately.
