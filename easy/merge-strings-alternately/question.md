# Merge Strings Alternately

You are given two strings, `word1` and `word2`. Construct a new string by merging them in alternating order, starting with `word1` — take one character from `word1`, then one from `word2`, and repeat this process.

If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result.

Return the final merged string.

## Example 1:

**Input:**  
word1 = "abc", word2 = "xyz"  
**Output:** "axbycz"

## Example 2:

**Input:**  
word1 = "ab", word2 = "abbxxc"  
**Output:** "aabbbxxc"

## Constraints:

- 1 <= word1.length, word2.length <= 100  
- `word1` and `word2` consist of lowercase English letters.
