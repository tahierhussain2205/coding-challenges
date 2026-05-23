from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Pointer to the last valid element in nums1's original portion
        nums1_left = m - 1
        # Pointer to the last position in nums1 (where merged elements get placed)
        nums1_right = len(nums1) - 1
        # Pointer to the last element in nums2
        nums2_right = n - 1

        # Fill nums1 from the back, picking the larger of the two current elements
        while nums1_left < nums1_right and nums2_right >= 0:

            # If nums2's current element is larger, place it at the back of nums1
            if nums2[nums2_right] > nums1[nums1_left]:
                nums1[nums1_right] = nums2[nums2_right]
                nums1_right -= 1
                nums2_right -= 1
                continue

            # Otherwise shift nums1's current element to the back
            nums1[nums1_right] = nums1[nums1_left]
            nums1[nums1_left] = 0
            nums1_left -= 1
            nums1_right -= 1

            # All of nums1's original elements have been placed
            if nums1_left == -1:
                break

        # Copy any remaining nums2 elements to the front of nums1
        for i in range(nums2_right + 1):
            nums1[i] = nums2[i]


# Test cases
solution = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
solution.merge(nums1, 3, [2, 5, 6], 3)
print(nums1)  # Expected: [1, 2, 2, 3, 5, 6]

nums1 = [4, 5, 6, 0, 0, 0]
solution.merge(nums1, 3, [1, 2, 3], 3)
print(nums1)  # Expected: [1, 2, 3, 4, 5, 6]


# Time Complexity: O(m + n)
#   - Each element from nums1 and nums2 is visited at most once.
#   - The while loop processes elements from the back, and the final
#     for loop handles any leftover nums2 elements.
#
# Space Complexity: O(1)
#   - Merge is done in-place within nums1 using only a few pointers.
#
# Approach:
#   Use a three-pointer approach working from the back of nums1.
#   Since nums1 has trailing zeros to accommodate nums2's elements,
#   we can safely place the larger of the two current elements at
#   the end without overwriting unprocessed data.
#
#   - nums1_left tracks the last valid element in nums1's original portion
#   - nums1_right tracks where the next merged element will be placed
#   - nums2_right tracks the last unprocessed element in nums2
#
#   At each step, compare nums1[nums1_left] and nums2[nums2_right],
#   placing the larger one at nums1[nums1_right]. Once nums1's elements
#   are exhausted, copy any remaining nums2 elements to the front.
