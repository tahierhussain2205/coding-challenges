from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            # Check if target is at the boundaries first
            if nums[left_pointer] == target:
                return left_pointer
            
            if nums[right_pointer] == target:
                return right_pointer

            mid_index = (left_pointer + right_pointer) // 2

            if nums[mid_index] == target:
                return mid_index

            # Case 1: Array is not rotated (normal sorted array)
            if nums[left_pointer] < nums[mid_index] < nums[right_pointer]:
                if target < nums[mid_index]:
                    right_pointer = mid_index - 1
                else:
                    left_pointer = mid_index + 1
                continue

            # Case 2: Rotation point is in the right half
            if nums[left_pointer] < nums[mid_index] and nums[mid_index] > nums[right_pointer]:
                if target > nums[left_pointer] and target < nums[mid_index]:
                    right_pointer = mid_index - 1
                else:
                    left_pointer = mid_index + 1
                continue

            # Case 3: Rotation point is in the left half
            if nums[left_pointer] > nums[mid_index] and nums[mid_index] < nums[right_pointer]:
                if target > nums[left_pointer] or target < nums[mid_index]:
                    right_pointer = mid_index - 1
                else:
                    left_pointer = mid_index + 1
                continue

            break

        return -1


# Test cases
solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))  # Expected: 4
print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))  # Expected: -1

# Time Complexity: O(log n) - Binary search approach
# Space Complexity: O(1) - Only using constant extra space
# 
# Algorithm: Modified binary search that handles rotated sorted arrays by
# identifying which half contains the rotation point and searching accordingly
