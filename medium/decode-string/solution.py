class Solution:

    def __init__(self):
        self.open_bracket = "["
        self.close_bracket = "]"

    def decodeString(self, s: str) -> str:
        """
        Recursively decode an encoded string using stack-based bracket matching.

        Algorithm:
        1. Iterate through each character in the string
        2. When encountering a digit, extract the full number (multiplier)
        3. Use a stack to find the matching closing bracket for the encoded substring
        4. Recursively decode the substring and multiply by the count
        5. Append regular characters directly to result
        """
        result = ""
        current_pos = 0

        while current_pos < len(s):
            # Process digits - indicates start of encoded pattern k[...]
            if s[current_pos].isdigit():
                # Extract the complete number (could be multi-digit like "10")
                num_start = current_pos
                num_str = ""

                while s[num_start].isdigit():
                    num_str += s[num_start]
                    num_start += 1

                repeat_count = int(num_str)
                # Start after the opening bracket '['
                bracket_pos = num_start
                # Stack to track nested brackets and find matching closing bracket
                bracket_stack = [s[bracket_pos]]
                encoded_substring = ""

                bracket_pos += 1
                # Use stack to handle nested brackets like "3[a2[c]]"
                while bracket_pos < len(s):
                    if s[bracket_pos] == self.open_bracket:
                        bracket_stack.append(s[bracket_pos])

                    if s[bracket_pos] == self.close_bracket:
                        bracket_stack.pop()

                    # Add character to substring if we're still inside brackets
                    if len(bracket_stack) != 0:
                        encoded_substring += s[bracket_pos]
                    else:
                        # Found matching closing bracket, exit loop
                        break

                    bracket_pos += 1

                # Recursively decode the substring and repeat it
                result += repeat_count * self.decodeString(encoded_substring)
                current_pos = bracket_pos + 1
                continue

            # Regular character - add directly to result
            result += s[current_pos]
            current_pos += 1

        return result


"""
COMPLEXITY ANALYSIS:

Time Complexity: O(n * m)
- n = length of input string
- m = maximum length of any decoded substring result
- We traverse the input string once, but recursive calls process substrings
- In worst case with deep nesting like "2[2[2[a]]]", each level multiplies the result length
- Each recursive call processes its substring completely

Space Complexity: O(d * s)  
- d = maximum nesting depth (recursion stack depth)
- s = maximum length of any substring stored during processing
- Recursion stack grows with nesting depth
- Additional space for bracket_stack and encoded_substring at each level

ALGORITHM WALKTHROUGH:
This solution uses a recursive approach with stack-based bracket matching:

1. Parse input character by character
2. When digit found: extract full number (handle multi-digit like "10")
3. Use bracket stack to find matching closing bracket for the encoded pattern
4. Recursively decode the inner substring
5. Multiply the decoded result by the repeat count
6. Continue processing remaining characters

OPTIMIZATION NOTES:
- Could be optimized to O(n) time using iterative two-stack approach
- Current recursive approach is intuitive but has overhead from function calls
- Stack-based bracket matching correctly handles nested patterns like "3[a2[c]]"
"""


solution = Solution()

# Test Case 1: Simple nested pattern
test1 = "3[a2[c]]"
result1 = solution.decodeString(test1)
print(f"Input: {test1}")
print(f"Output: {result1}")
print(f"Expected: accaccacc")
print(f"Correct: {result1 == 'accaccacc'}")
print()

# Test Case 2: Multiple patterns with regular characters
test2 = "2[abc]3[cd]ef"
result2 = solution.decodeString(test2)
print(f"Input: {test2}")
print(f"Output: {result2}")
print(f"Expected: abcabccdcdcdef")
print(f"Correct: {result2 == 'abcabccdcdcdef'}")
