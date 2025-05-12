# Top K Frequent Elements

**Problem**  
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements within the array.

You may return the answer in **any order**.

The test cases are generated such that the answer is always **unique**.

---

### Examples

**Example 1**  
**Input:**  
`nums = [1,2,2,3,3,3]`, `k = 2`  
**Output:**  
`[2,3]`

**Example 2**  
**Input:**  
`nums = [7,7]`, `k = 1`  
**Output:**  
`[7]`

---

### Constraints

- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`
- `1 <= k <= number of distinct elements in nums`

---

### Follow-up

Can you solve it in **O(n)** time complexity?

---

### Solution Overview

This problem can be efficiently solved using the **bucket sort algorithm** by grouping elements based on their frequency. This allows us to avoid the O(n log n) cost of sorting the entire list based on frequency.
