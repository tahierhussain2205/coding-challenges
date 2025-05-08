from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Convert the list to a set to remove duplicates
        # If the length reduces, it means there were duplicates
        return len(nums) > len(set(nums))


solution = Solution()

# Test case 1: has duplicates
# 1 appears twice, so the function should return True
nums1 = [1, 2, 3, 4, 1]
print(solution.hasDuplicate(nums1))  # Output: True

# Test case 2: no duplicates
# All elements are unique, so the function should return False
nums2 = [5, 6, 7, 8, 9]
print(solution.hasDuplicate(nums2))  # Output: False

"""
Note:
Time Complexity: O(n)
- Converting the list to a set takes O(n) time in the average case.

Space Complexity: O(n)
- In the worst case (all unique elements), the set stores all n elements.
"""
