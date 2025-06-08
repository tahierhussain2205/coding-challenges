from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Set of valid operators
        operators = {"+", "-", "*", "/"}
        # Stack to store operands
        stack = []

        # Loop through each token in the input list
        for token in tokens:
            if token not in operators:
                # If it's a number, convert to int and push to the stack
                stack.append(int(token))
                continue

            # Pop the top two operands from the stack
            right_operand = stack.pop()
            left_operand = stack.pop()

            # Perform the operation based on the operator
            if token == "+":
                result = left_operand + right_operand
            elif token == "-":
                result = left_operand - right_operand
            elif token == "*":
                result = left_operand * right_operand
            elif token == "/":
                # Division that truncates toward zero
                result = int(left_operand / right_operand)

            # Push the result back onto the stack
            stack.append(result)

        # The final result will be the only element left in the stack
        return stack[0]


# ✅ Test cases
solution = Solution()
print(solution.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9 → ((2 + 1) * 3)
print(solution.evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6 → (4 + (13 / 5))
# Output: 22 → ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

"""
Time Complexity: O(n)
- Each token is processed once.
- Stack operations (append/pop) are O(1).
- Total time = O(n) where n = number of tokens.

Space Complexity: O(n)
- In the worst case (all numbers before any operator), the stack can hold up to n elements.
- So, auxiliary space = O(n).
"""
