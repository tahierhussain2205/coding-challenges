from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize result prefix
        longest_prefix = ""

        # Get the length of the first string to use as upper bound
        first_str_length = len(strs[0])

        # Flag to break early from outer loop
        should_break = False

        # Loop over each character position (column-wise)
        for i in range(first_str_length):
            current_char = ""

            # Compare the character at position 'i' in all strings
            for word in strs:
                # If any string is shorter than current index, stop
                if len(word) <= i:
                    should_break = True
                    break

                # Initialize current_char if not set
                if not current_char:
                    current_char = word[i]
                    continue

                # If there's a mismatch, stop
                if word[i] != current_char:
                    should_break = True
                    break

            if should_break:
                break

            # All strings had the same character at this position
            longest_prefix += current_char

        return longest_prefix


# ✅ Test cases
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))       # Output: "fl"
print(solution.longestCommonPrefix(["bat", "bag", "bank", "band"]))     # Output: "ba"
print(solution.longestCommonPrefix(["neet", "feet"]))                   # Output: ""

# ✅ Time and Space Complexity:
# Time Complexity: O(S), where S is the total number of characters in all strings
# Space Complexity: O(1) (excluding the output string)
