from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        open_paren = "("
        close_paren = ")"
        # We need to build strings of length 2*n, starting with one '(' already placed
        iterations_needed = (n * 2) - 2

        # Start with a list containing just the first opening parenthesis
        current_combinations = [open_paren]

        # Build combinations character by character through BFS-style generation
        for i in range(iterations_needed):
            next_combinations = []

            # For each current combination, try adding both '(' and ')' if valid
            for combination in current_combinations:
                open_count = 0
                close_count = 0

                # Count existing parentheses in current combination
                for char in combination:
                    if char == open_paren:
                        open_count += 1
                    else:
                        close_count += 1

                # Add opening parenthesis if we haven't used all n opening parens
                # and if it maintains validity (open_count >= close_count)
                if open_count < n and open_count >= close_count:
                    next_combinations.append(combination + open_paren)

                # Add closing parenthesis if we haven't used all n closing parens
                # and if there are unmatched opening parens (close_count < open_count)
                if close_count < n and close_count < open_count:
                    next_combinations.append(combination + close_paren)

            current_combinations = next_combinations

        # Add final closing parenthesis to complete all combinations
        for index, combination in enumerate(current_combinations):
            current_combinations[index] = combination + close_paren

        return current_combinations


# Test cases
solution = Solution()
print("Test case 1 - n=3:")
print(solution.generateParenthesis(3))
print("\nTest case 2 - n=1:")
print(solution.generateParenthesis(1))

"""
Time Complexity Analysis:
- Current: O(n × 4^n)
  - We iterate (2n-2) times, and in each iteration we process all combinations
  - For each combination, we count parentheses which takes O(n) time
  - The number of combinations grows exponentially, roughly 4^n in worst case

Space Complexity Analysis:
- Current: O(4^n)
  - We store all intermediate combinations at each level
  - Multiple lists are created and maintained throughout the process

Future Improvements:
- Target: O(4^n / √n) time and space complexity (Catalan number bound)
"""
