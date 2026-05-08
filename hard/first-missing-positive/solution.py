from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Convert to set for O(1) lookups when checking for missing positives
        nums_set = set(nums)
        max_value = max(nums_set)

        # Scan positive integers from 1 upward; the first one missing is the answer
        for candidate in range(1, max_value):
            if candidate not in nums_set:
                return candidate

        # If every value from 1..max_value exists, the answer is max_value + 1
        if max_value > 0:
            return max_value + 1

        # All values are non-positive, so 1 is the smallest missing positive
        return 1


solution = Solution()
print(solution.firstMissingPositive([3, 4, -1, 1]))  # Expected: 2
print(solution.firstMissingPositive([7, 8, 9, 11, 12]))  # Expected: 1

# Time Complexity: O(n)
#   - Building the set: O(n)
#   - Finding max_value: O(n)
#   - Scanning range(1, max_value): O(n) in the worst case (when values are dense in [1, n])
#
# Space Complexity: O(n)
#   - The set stores up to n elements
#   - Note: this does not meet the problem's O(1) auxiliary space requirement;
#     achieving that requires in-place index marking (cyclic sort or sign-flipping)
#
# Algorithm Walkthrough:
#   1. Put all numbers in a set for constant-time membership checks.
#   2. Iterate positive integers starting at 1. The first integer not in the set
#      is the smallest missing positive.
#   3. If the loop completes without finding a gap, the array contains 1..max_value
#      contiguously, so the answer is max_value + 1 (when max_value is positive).
#   4. If max_value is non-positive, no positive integers exist in the array, so 1
#      is the smallest missing positive.
