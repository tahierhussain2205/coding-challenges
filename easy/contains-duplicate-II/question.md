# 🧩 Problem: Contains Duplicate II

You are given an integer array `nums` and an integer `k`.

Return `true` if there are **two distinct indices** `i` and `j` in the array such that:

- `nums[i] == nums[j]`
- and `abs(i - j) <= k`

Otherwise, return `false`.

---

## ✨ Examples

### Example 1:

**Input:**
```
nums = [1, 2, 3, 1]
k = 3
```

**Output:** `true`

**Explanation:** `nums[0] == nums[3]` and `abs(0 - 3) = 3 <= 3`.

---

### Example 2:

**Input:**
```
nums = [2, 1, 2]
k = 1
```

**Output:** `false`

**Explanation:** Even though `nums[0] == nums[2]`, `abs(0 - 2) = 2 > 1`.

---

## 🔒 Constraints

- `1 <= nums.length <= 100,000`
- `-1,000,000,000 <= nums[i] <= 1,000,000,000`
- `0 <= k <= 100,000`