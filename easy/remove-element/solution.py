from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total_length = len(nums)
        current_pos = 0
        removed_count = 0

        # Two-pointer approach: scan from the left, swap matches to the right end
        while current_pos + removed_count < total_length:

            if nums[current_pos] == val:
                # Swap the matching element with the last unprocessed element
                last_unprocessed = total_length - removed_count - 1
                nums[current_pos], nums[last_unprocessed] = nums[last_unprocessed], nums[current_pos]
                removed_count += 1
            else:
                current_pos += 1

        # Number of elements that are not equal to val
        return total_length - removed_count


solution = Solution()

# Test Case 1: Multiple occurrences of val scattered throughout
nums1 = [0, 1, 2, 2, 3, 0, 4, 2]
k1 = solution.removeElement(nums1, 2)
print(f"k = {k1}, nums = {nums1[:k1]}")  # Expected: k = 5, nums first 5 contain [0,1,3,0,4] in any order

# Test Case 2: val not present in array
nums2 = [3, 2, 2, 3]
k2 = solution.removeElement(nums2, 3)
print(f"k = {k2}, nums = {nums2[:k2]}")  # Expected: k = 2, nums first 2 contain [2,2] in any order

# Time Complexity: O(n)
#   - Each iteration either advances current_pos or increments removed_count
#   - The loop terminates when current_pos + removed_count == n, so at most n iterations
#
# Space Complexity: O(1)
#   - Modifies the input array in place using only a constant number of variables
#
# Algorithm Walkthrough:
#   - Use two pointers: current_pos scans from the left, and (total_length - removed_count - 1)
#     tracks the last unprocessed element on the right.
#   - When nums[current_pos] equals val, swap it with the last unprocessed element and
#     increment removed_count, effectively pushing matches to the end of the array.
#   - When nums[current_pos] does not equal val, advance current_pos to keep it in place.
#   - The loop ends when the two pointers meet, and the first (total_length - removed_count)
#     elements are the kept values.
