from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store value -> index mapping
        num_to_index = {}
        get_index = num_to_index.get  # Local binding for slight performance gain

        for current_index in range(len(nums)):
            current_value = nums[current_index]
            complement = target - current_value

            # Check if the complement exists in the map
            if get_index(complement) is not None:
                return [num_to_index[complement], current_index]

            # Store the current value with its index
            num_to_index[current_value] = current_index


# Example usage
solution = Solution()

# Test Case 1
nums1 = [5, 5]
target1 = 10
print(solution.twoSum(nums1, target1))  # Output: [0, 1]

# Test Case 2
nums2 = [2, 7, 11, 15]
target2 = 9
print(solution.twoSum(nums2, target2))  # Output: [0, 1]

# Test Case 3
nums3 = [3, 1, 4, 6, 5]
target3 = 7
print(solution.twoSum(nums3, target3))  # Output: [1, 4]

"""
Note:
Local binding (like assigning `get_index = num_to_index.get`) provides a slight performance benefit
in tight loops. This is because accessing a local variable in Python is faster than repeatedly performing
an attribute lookup like `num_to_index.get` on every iteration. Although the gain is minimal, it can add up
in performance-critical code that runs millions of times.
"""
