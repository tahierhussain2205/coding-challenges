from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Calculate the sum of valid scores after applying baseball game operations.

        Uses a stack to maintain the record of scores and processes each operation:
        - Integer: Add new score to record
        - '+': Add sum of last two scores
        - 'D': Add double of last score  
        - 'C': Cancel/remove last score

        Args:
            operations: List of operation strings

        Returns:
            Sum of all valid scores in the final record
        """
        score_record = []  # Stack to maintain the current valid scores

        # Process each operation in sequence
        for current_operation in operations:
            if current_operation == "+":
                # Add sum of the previous two scores
                sum_of_last_two = score_record[-1] + score_record[-2]
                score_record.append(sum_of_last_two)

            elif current_operation == "D":
                # Add double of the previous score
                double_last_score = score_record[-1] * 2
                score_record.append(double_last_score)

            elif current_operation == "C":
                # Cancel/invalidate the previous score
                score_record.pop()

            else:
                # Integer score - convert string to int and add to record
                numeric_score = int(current_operation)
                score_record.append(numeric_score)

        # Return the sum of all remaining valid scores
        return sum(score_record)


solution = Solution()

# Test case 1: Example from problem description
test_case_1 = ["5", "2", "C", "D", "+"]
result_1 = solution.calPoints(test_case_1)
print(f"Test 1: {test_case_1} -> {result_1} (Expected: 30)")

# Test case 2: More complex example with negative numbers
test_case_2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
result_2 = solution.calPoints(test_case_2)
print(f"Test 2: {test_case_2} -> {result_2} (Expected: 27)")


"""
Complexity Analysis:

Time Complexity: O(n)
- We iterate through each operation exactly once
- Each operation (append, pop, sum calculation) takes O(1) time
- Final sum calculation takes O(k) where k is the number of remaining scores
- Since k ≤ n, overall time complexity is O(n)

Space Complexity: O(n)
- In the worst case, we might store all n operations as scores in our stack
- This happens when there are no 'C' operations to remove scores
- The score_record list can grow up to size n in the worst case

Algorithm Explanation:
1. Use a stack (list) to maintain the current valid scores
2. Process each operation sequentially:
   - For integers: Convert to int and push to stack
   - For '+': Sum last two scores and push result
   - For 'D': Double last score and push result  
   - For 'C': Remove/pop the last score
3. Return sum of all remaining scores in the stack

Key Insights:
- Stack is perfect for this problem since we only need to access recent scores
- By storing actual integer values instead of strings, we avoid repeated conversions
- The problem guarantees all operations are valid, so no error checking needed
"""
