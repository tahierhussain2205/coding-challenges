from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            mid_index = (left_pointer + right_pointer) // 2

            # Check if target is found at any of the key positions
            if nums[mid_index] == target or nums[left_pointer] == target or nums[right_pointer] == target:
                return True

            # Handle duplicates: if left equals mid, move left pointer
            if nums[left_pointer] == nums[mid_index]:
                left_pointer += 1
                continue

            # Handle duplicates: if right equals mid, move right pointer
            if nums[right_pointer] == nums[mid_index]:
                right_pointer -= 1
                continue

            # Case 1: No rotation in current segment (sorted array)
            if nums[left_pointer] < nums[mid_index] and nums[mid_index] < nums[right_pointer]:
                if target < nums[mid_index]:
                    right_pointer = mid_index - 1
                else:
                    left_pointer = mid_index + 1
                continue

            # Case 2: Left side is sorted, right side contains rotation point
            if nums[left_pointer] < nums[mid_index] and nums[mid_index] > nums[right_pointer]:
                if target >= nums[left_pointer] and target < nums[mid_index]:
                    right_pointer = mid_index - 1
                else:
                    left_pointer = mid_index + 1
                continue

            # Case 3: Right side is sorted, left side contains rotation point
            if nums[left_pointer] > nums[mid_index] and nums[mid_index] < nums[right_pointer]:
                if target > nums[mid_index] and target <= nums[right_pointer]:
                    left_pointer = mid_index + 1
                else:
                    right_pointer = mid_index - 1

        return False


# Test cases
solution = Solution()
print(solution.search([3, 4, 4, 5, 6, 1, 2, 2], 1))  # Expected: True
print(solution.search([3, 5, 6, 0, 0, 1, 2], 4))    # Expected: False

# Time Complexity: O(n) worst case due to duplicates, O(log n) average case
# - In worst case with many duplicates, we may need to linearly scan
# - Average case maintains binary search efficiency when few duplicates exist
# Space Complexity: O(1) - only using constant extra space for pointers
#
# Algorithm: Modified binary search for rotated sorted array with duplicates
# 1. Use three pointers: left, right, and mid to narrow search space
# 2. Handle duplicates by incrementally moving pointers when values equal mid
# 3. Determine which side is sorted and search accordingly:
#    - If no rotation: standard binary search
#    - If left side sorted: check if target in left range, otherwise search right
#    - If right side sorted: check if target in right range, otherwise search left
