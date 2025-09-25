# Split Array Largest Sum (Hard)

You are given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

## Examples

### Example 1:
```
Input: nums = [2,4,10,1,5], k = 2
Output: 16
Explanation: The best way is to split into [2,4,10] and [1,5], where the largest sum among the two subarrays is only 16.
```

### Example 2:
```
Input: nums = [1,0,2,3,5], k = 4
Output: 5
Explanation: The best way is to split into [1], [0,2], [3] and [5], where the largest sum among the two subarrays is only 5.
```

## Constraints

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1,000,000`
- `1 <= k <= min(50, nums.length)`