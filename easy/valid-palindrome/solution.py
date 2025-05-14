class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_index, right_index = 0, len(s) - 1

        # Loop until the pointers meet in the middle
        while left_index < right_index:
            # Skip non-alphanumeric characters on the left
            while left_index < right_index and not self.isAlphanumeric(s[left_index]):
                left_index += 1

            # Skip non-alphanumeric characters on the right
            while left_index < right_index and not self.isAlphanumeric(s[right_index]):
                right_index -= 1

            # Compare lowercase versions of both characters
            if s[left_index].lower() != s[right_index].lower():
                return False

            left_index += 1
            right_index -= 1

        return True

    def isAlphanumeric(self, char: str) -> bool:
        # ✅ Custom implementation using ASCII value ranges
        # This was purposefully written to experiment with ASCII logic
        # and to avoid using Python’s built-in str.isalnum().
        ascii_val = ord(char)
        return (
            ord('a') <= ascii_val <= ord('z') or
            ord('A') <= ascii_val <= ord('Z') or
            ord('0') <= ascii_val <= ord('9')
        )


# ✅ Test cases
solution = Solution()
print(solution.isPalindrome("Was it a car or a cat I saw?"))  # Output: True
print(solution.isPalindrome("tab a cat"))                      # Output: False


"""
🧠 Time Complexity: O(n)
- Each character is visited at most once by either pointer.

📦 Space Complexity: O(1)
- Only uses two integer pointers and simple variables.

✅ This approach keeps full control of character checking by using a custom ASCII-based `isAlphanumeric()` function,
which was purposefully implemented to experiment with ASCII ranges and avoid Python’s built-in `isalnum()`.
"""
