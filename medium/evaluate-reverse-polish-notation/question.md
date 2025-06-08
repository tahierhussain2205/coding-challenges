# 🧮 Evaluate Reverse Polish Notation

You are given an array of strings `tokens` that represents a valid arithmetic expression in **Reverse Polish Notation**.

Return the **integer** that represents the evaluation of the expression.

---

## 🔧 Operators supported:
- `'+'` → addition
- `'-'` → subtraction
- `'*'` → multiplication
- `'/'` → division (integer division that **truncates toward zero**)

---

## 💡 Notes:
- The operands may be integers or the results of other operations.
- Division between integers always truncates toward zero.

---

## ✅ Example 1:
**Input:**  
`tokens = ["1", "2", "+", "3", "*", "4", "-"]`  
**Output:**  
`5`  
**Explanation:**  
((1 + 2) * 3) - 4 = 5

---

## ✅ Example 2:
**Input:**  
`tokens = ["2", "1", "+", "3", "*"]`  
**Output:**  
`9`  
**Explanation:**  
(2 + 1) * 3 = 9

---

## 🔒 Constraints:
- `1 <= tokens.length <= 1000`
- `tokens[i]` is `"+"`, `"-"`, `"*"`, `"/"`, or a string representing an integer in the range `[-100, 100]`

---

## 🔁 Function Signature

```python
def evalRPN(tokens: List[str]) -> int:
```