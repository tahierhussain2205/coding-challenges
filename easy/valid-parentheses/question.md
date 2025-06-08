# 🧩 Valid Parentheses

You are given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`.

---

## ✅ A string is considered **valid** if:

1. Every open bracket is closed by the **same type** of close bracket.
2. Open brackets are closed in the **correct order**.
3. Every close bracket has a **corresponding open bracket** of the same type.

---

## ✏️ Example 1:

**Input:**  
`s = "[]"`  
**Output:**  
`true`

---

## ✏️ Example 2:

**Input:**  
`s = "([{}])"`  
**Output:**  
`true`

---

## ✏️ Example 3:

**Input:**  
`s = "[(])"`  
**Output:**  
`false`  
**Explanation:**  
The brackets are not closed in the correct order.

---

## 🔒 Constraints:

- `1 <= s.length <= 1000`
