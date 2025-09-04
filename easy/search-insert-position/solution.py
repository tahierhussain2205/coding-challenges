from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Binary search - find leftmost position where target can be inserted
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # left now points to the insertion position
        return left


# Test cases
solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))  # Expected: 2
print(solution.searchInsert([1, 3, 5, 6], 2))  # Expected: 1

# Time Complexity: O(log n) - Pure binary search with no additional linear work
# Space Complexity: O(1) - Only using constant extra space for pointers
# Algorithm: Standard binary search that converges to the exact insertion position
