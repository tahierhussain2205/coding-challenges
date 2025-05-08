class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are not equal, they can't be anagrams
        if len(s) != len(t):
            return False

        count_map = {}  # Dictionary to store character frequency differences

        # Iterate through both strings simultaneously
        for i in range(len(s)):
            # Increment count for character from s
            count_map[s[i]] = count_map.get(s[i], 0) + 1

            # Decrement count for character from t
            count_map[t[i]] = count_map.get(t[i], 0) - 1

        # If all counts are zero, it's a valid anagram
        return all(value == 0 for value in count_map.values())


# Example 1
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True

# Example 2
print(solution.isAnagram("rat", "car"))          # Output: False

"""
Note:
Time Complexity: O(n), where n is the length of the strings
Space Complexity: O(1), since the dictionary holds at most 26 lowercase letters
"""
