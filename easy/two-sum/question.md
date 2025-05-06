# Two Sum

**Difficulty**: Easy  
**Platform**: LeetCode (or general practice)

---

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that **exactly one solution** exists.  
Return the answer with the **smaller index first**.

---

## Examples

### Example 1

**Input**:  
`nums = [3, 4, 5, 6]`, `target = 7`  
**Output**:  
`[0, 1]`  
**Explanation**: `nums[0] + nums[1] = 3 + 4 = 7`

---

### Example 2

**Input**:  
`nums = [4, 5, 6]`, `target = 10`  
**Output**:  
`[0, 2]`

---

### Example 3

**Input**:  
`nums = [5, 5]`, `target = 10`  
**Output**:  
`[0, 1]`

---

## Constraints

- `2 <= nums.length <= 1000`
- `-10,000,000 <= nums[i] <= 10,000,000`
- `-10,000,000 <= target <= 10,000,000`
