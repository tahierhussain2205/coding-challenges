from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        left_index = 0
        right_index = len(numbers) - 1

        # Continue searching while left pointer is to the left of right pointer
        while left_index < right_index:
            current_sum = numbers[left_index] + numbers[right_index]

            # If the current sum is greater than target, move the right pointer leftward
            while left_index < right_index and current_sum > target:
                right_index -= 1
                current_sum = numbers[left_index] + numbers[right_index]

            # If the current sum is less than target, move the left pointer rightward
            while left_index < right_index and current_sum < target:
                left_index += 1
                current_sum = numbers[left_index] + numbers[right_index]

            # If a valid pair is found, return their 1-based indices
            if current_sum == target:
                return [left_index + 1, right_index + 1]

        # This return is a fallback and should never be hit as per problem constraints
        return []


# ✅ Test Cases
solution = Solution()

# Test Case 1
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]

# Test Case 2
print(solution.twoSum([1, 2, 3, 4, 6], 10))  # Output: [4, 5]

"""
Time Complexity: O(n)
- We move the two pointers (left and right) inward at most n times combined.
- No nested iterations over the array, just linear traversal.

Space Complexity: O(1)
- We use only two pointer variables, regardless of input size.
- No additional space or data structures are used.
"""
