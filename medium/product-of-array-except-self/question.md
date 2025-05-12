# Products of Array Except Self

**Problem**  
Given an integer array `nums`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Each product is guaranteed to fit in a 32-bit integer.

---

### Follow-up

Can you solve it in **O(n)** time **without using the division operation**?

---

### Examples

**Example 1**  
**Input:**  
`nums = [1, 2, 4, 6]`  
**Output:**  
`[48, 24, 12, 8]`

**Example 2**  
**Input:**  
`nums = [-1, 0, 1, 2, 3]`  
**Output:**  
`[0, -6, 0, 0, 0]`

---

### Constraints

- `2 <= nums.length <= 1000`
- `-20 <= nums[i] <= 20`

---

### Explanation

You are required to return an array where each element is the product of all other elements in the array, except itself. The challenge is to do it in **linear time** and ideally without using division.

This problem can be efficiently solved using the prefix and suffix product technique or a careful handling of zero cases if division is used.
