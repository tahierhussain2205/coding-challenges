from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Track current position and where reds end
        current_index = 0
        red_boundary = 0
        array_length = len(nums)

        while current_index < array_length:
            # Move all reds (0s) to the front
            if nums[current_index] == 0:
                nums.pop(current_index)
                nums.insert(0, 0)
                red_boundary += 1

            # Move whites (1s) right after reds
            if nums[current_index] == 1:
                nums.pop(current_index)
                nums.insert(red_boundary, 1)

            current_index += 1

        return nums


# Test case 1
solution = Solution()
test1 = [2, 0, 2, 1, 1, 0]
solution.sortColors(test1)
print(test1)  # Expected: [0, 0, 1, 1, 2, 2]

# Test case 2
test2 = [2, 0, 1]
solution.sortColors(test2)
print(test2)  # Expected: [0, 1, 2]

"""
Time Complexity: O(n^2)
- Single pass through array: O(n)
- Each pop() and insert() operation: O(n) in worst case
- Overall: O(n) * O(n) = O(n^2)

Space Complexity: O(1)
- Only using constant extra space for variables (current_index, red_boundary, array_length)
- Sorting is done in-place

Algorithm Explanation:
This solution uses a counting approach that moves colors to their correct positions:
1. Iterate through the array once
2. When we find a red (0), move it to the front and track the red boundary
3. When we find a white (1), move it right after the reds
4. Blues (2) naturally end up at the end without explicit handling
5. The algorithm maintains the relative order by tracking where each color region ends
"""
