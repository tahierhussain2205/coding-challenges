from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold sorted string as key and list of anagrams as value
        grouped_anagrams = {}

        # Iterate over each word in the input list
        for word in strs:
            # Sort the word to get the key
            sorted_word = "".join(sorted(word))  # O(k log k), where k = length of the word

            # If the sorted word is already a key, append the original word to the list
            if sorted_word in grouped_anagrams:
                grouped_anagrams[sorted_word].append(word)
            else:
                # Else, create a new entry with the current word in a list
                grouped_anagrams[sorted_word] = [word]

        # Return the grouped list of anagrams
        return list(grouped_anagrams.values())


# Test cases
solution = Solution()

# Test case 1
# "eat", "tea", and "ate" are anagrams
# "tan" and "nat" are anagrams
# "bat" has no anagram pair
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Test case 2
# "abc" and "cab" are anagrams
# "bca" is also an anagram of "abc"
# "xyz" has no anagram pair
print(solution.groupAnagrams(["abc", "cab", "xyz", "bca"]))
# Output: [['abc', 'cab', 'bca'], ['xyz']]


"""
Time Complexity:
- Sorting each word takes O(k log k), where k = length of the word.
- For n words, total time = O(n * k log k)

Space Complexity:
- O(n * k) to store grouped anagrams in the dictionary
"""
