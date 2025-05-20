class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_chars = []
        min_length = min(len(word1), len(word2))

        # Merge characters from both strings one by one
        for i in range(min_length):
            merged_chars.append(word1[i])
            merged_chars.append(word2[i])

        # Append remaining characters (if any) from the longer word
        merged_chars.append(word1[min_length:])
        merged_chars.append(word2[min_length:])

        # Join the list into a final string
        return "".join(merged_chars)


# ✅ Test Cases
solution = Solution()

print(solution.mergeAlternately("abc", "pqr"))          # Output: "apbqcr"
print(solution.mergeAlternately("ab", "abbxxc"))        # Output: "aabbbxxc"
print(solution.mergeAlternately("abc111", "pqr"))       # Output: "apbqcr111"

"""
Time Complexity: O(n)
- Where n = len(word1) + len(word2)
- Each character is processed once and then joined in a single pass.

Space Complexity: O(n)
- Additional space is used to store the merged result as a list of characters.
"""
