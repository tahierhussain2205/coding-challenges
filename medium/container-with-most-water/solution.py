from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers at both ends of the array
        left = 0
        right = len(height) - 1

        max_area = 0  # To keep track of the maximum area found

        # Move the pointers toward each other
        while left < right:
            # Calculate the width between the two lines
            width = right - left

            # Calculate the height by choosing the shorter line
            current_height = min(height[left], height[right])

            # Calculate the area and update max_area if this is larger
            current_area = width * current_height
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# ✅ Test cases
solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))     # Output: 49
print(solution.maxArea([1, 2, 3, 1000, 9]))              # Output: 9
print(solution.maxArea([5, 2, 12, 1, 5, 3, 4, 11, 9, 4]))  # Output: 44

"""
Time Complexity: O(n)
  - We traverse the list once using two pointers.
  - Each element is considered at most once.

Space Complexity: O(1)
  - We use a constant amount of extra space regardless of input size.
"""
