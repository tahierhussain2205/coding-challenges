class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_len = len(s)

        # Edge case: Single character string
        if str_len == 1:
            return 1

        # Dictionary to store the most recent index of each character
        char_index_map = {}
        left_ptr = 0  # Left boundary of the sliding window
        max_substring_length = 0

        for right_ptr in range(str_len):
            current_char = s[right_ptr]

            # If character is not in the current window or not seen before
            if current_char not in char_index_map:
                char_index_map[current_char] = right_ptr
                continue

            # If the character was seen before but outside the current window
            if char_index_map[current_char] < left_ptr:
                char_index_map[current_char] = right_ptr
                continue

            # Character is inside the current window, update max length
            max_substring_length = max(max_substring_length, right_ptr - left_ptr)

            # Move left pointer just after the previous occurrence of the duplicate character
            left_ptr = char_index_map[current_char] + 1

            # Update the index of the current character
            char_index_map[current_char] = right_ptr

        # Final comparison for substring from last unique segment
        return max(max_substring_length, str_len - left_ptr)


# Example usage
solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))     # Output: 3
print(solution.lengthOfLongestSubstring("abcabcbb"))   # Output: 3

"""
Time Complexity: O(n)
- Each character is processed once, and dictionary operations are O(1) on average.

Space Complexity: O(k)
- Where k is the number of unique characters in the input string.
- In case of ASCII input, k is at most 128, making space complexity effectively O(1).
"""
