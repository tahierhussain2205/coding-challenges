from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


solution = Solution()

# Test case 1: has duplicates
nums1 = [1, 2, 3, 4, 1]
print(solution.hasDuplicate(nums1))  # Output: True

# Test case 2: no duplicates
nums2 = [5, 6, 7, 8, 9]
print(solution.hasDuplicate(nums2))  # Output: False
