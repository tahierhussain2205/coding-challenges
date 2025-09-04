from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        
        # Binary search to find minimum element in rotated sorted array
        while left_pointer < right_pointer:
            mid_pointer = (left_pointer + right_pointer) // 2
            
            # If mid element is greater than rightmost, minimum is in right half
            if nums[mid_pointer] > nums[right_pointer]:
                left_pointer = mid_pointer + 1
            else:
                # Otherwise, minimum is in left half (including mid)
                right_pointer = mid_pointer
        
        # left_pointer now points to the minimum element
        return nums[left_pointer]


# Test cases
solution = Solution()
print(solution.findMin([3, 4, 5, 1, 2]))    # Expected: 1
print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))  # Expected: 0

# Time Complexity: O(log n) - Binary search reduces search space by half each iteration
# Space Complexity: O(1) - Only using constant extra space for pointers
# Algorithm: Compare mid with right to determine which half contains the rotation point (minimum)
