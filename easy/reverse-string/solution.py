from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        length = len(s)
        # Swap characters from both ends moving toward the center
        for i in range(length // 2):
            s[i], s[length - i - 1] = s[length - i - 1], s[i]


# ✅ Test cases
solution = Solution()

# Test Case 1
chars1 = ["n", "e", "e", "t"]
solution.reverseString(chars1)
print(chars1)  # Output: ['t', 'e', 'e', 'n']

# Test Case 2
chars2 = ["r", "a", "c", "e", "c", "a", "r"]
solution.reverseString(chars2)
print(chars2)  # Output: ['r', 'a', 'c', 'e', 'c', 'a', 'r']

# ✅ Time and Space Complexity:

# Time Complexity: O(n)
# ---------------------
# The loop runs for n/2 iterations where n is the length of the input list.
# Each iteration performs a constant-time swap operation.
# Hence, total time is proportional to the number of characters: O(n)

# Space Complexity: O(1)
# ----------------------
# Only a single temporary variable is used for swapping.
# The reversal is done in-place without using extra memory.
# Hence, space complexity is constant: O(1)
