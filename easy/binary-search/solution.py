from typing import List

class Solution:
    def search(self, sorted_nums: List[int], target_value: int) -> int:
        # Initialize the search boundaries
        start_index, end_index = 0, len(sorted_nums) - 1
        
        # Continue the loop until the search space is exhausted
        while start_index <= end_index:
            # Calculate the middle index
            middle_index = (start_index + end_index) // 2

            # If the middle element matches the target, return its index
            if sorted_nums[middle_index] == target_value:
                return middle_index
            # If the middle element is less than the target, narrow search to the right half
            elif sorted_nums[middle_index] < target_value:
                start_index = middle_index + 1
            # If the middle element is greater than the target, narrow search to the left half
            else:
                end_index = middle_index - 1

        # Target was not found in the array
        return -1


# ✅ Test cases
solution = Solution()

# Test case 1: Target exists in the array
print(solution.search([-1, 0, 2, 4, 6, 8], 4))  # Output: 3

# Test case 2: Target does not exist in the array
print(solution.search([-1, 0, 2, 4, 6, 8], 3))  # Output: -1

# Test case 3: Single element array where target matches
print(solution.search([5], 5))  # Output: 0


"""
🧠 Time Complexity:
- O(log n), where n is the number of elements in the array.
- At each step, the algorithm halves the search space.

🧠 Space Complexity:
- O(1), because no extra space is used aside from a few pointers.
"""
