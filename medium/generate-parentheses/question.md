# Generate Parentheses

## Problem

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

---

## Example 1:

**Input:**  
`n = 3`  
**Output:**  
`["((()))","(()())","(())()","()(())","()()()"]`

## Example 2:

**Input:**  
`n = 1`  
**Output:**  
`["()"]`

---

## Constraints

- 1 <= n <= 8

---

## Recommended Time & Space Complexity

You should aim for a solution with:

- **Time Complexity:** O(4^n / √n) (Catalan number)  
- **Space Complexity:** O(4^n / √n)