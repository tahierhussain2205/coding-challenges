class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map opening brackets to their corresponding closing brackets
        bracket_pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        # Stack to keep track of opening brackets
        open_brackets = []

        # Traverse each character in the string
        for char in s:
            if char in bracket_pairs:
                # If it's an opening bracket, push to stack
                open_brackets.append(char)
            else:
                # If it's a closing bracket, check if stack is empty
                if not open_brackets:
                    return False  # No matching opening bracket

                # Pop the last opening bracket
                last_open = open_brackets.pop()

                # Check if it matches the expected closing bracket
                if bracket_pairs[last_open] != char:
                    return False  # Mismatched pair

        # If stack is empty, all brackets matched correctly
        return len(open_brackets) == 0


# ✅ Test cases
solution = Solution()
print(solution.isValid("()[]{}"))     # True — all brackets are properly closed and ordered
print(solution.isValid("([{}])"))     # True — nested and ordered properly
print(solution.isValid("[(])"))       # False — incorrect order of closing

"""
Time Complexity: O(n)
- We iterate through the string once — each character is processed once.
- Stack operations (append/pop) are O(1), so total is linear in n.

Space Complexity: O(n)
- In the worst case, we may store all opening brackets in the stack.
- Hence, stack can grow up to size n.
"""
