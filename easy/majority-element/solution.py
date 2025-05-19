from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Step 1: Sort the array
        # The majority element is guaranteed to appear more than ⌊n / 2⌋ times,
        # so it will always occupy the middle index after sorting
        return sorted(nums)[len(nums) // 2]


# ✅ Test cases
solution = Solution()
print(solution.majorityElement([3, 2, 3]))               # Output: 3
print(solution.majorityElement([5, 5, 1, 1, 1, 5, 5]))   # Output: 5

# ✅ Time and Space Complexity:

# Time Complexity: O(n log n)
# ---------------------------
# The sorting operation takes O(n log n) time where n is the length of the array.
# Accessing the middle index is a constant-time operation: O(1)

# Space Complexity: O(n)
# -----------------------
# The sorted() function creates a new list rather than sorting in place,
# which takes O(n) additional space in Python.
