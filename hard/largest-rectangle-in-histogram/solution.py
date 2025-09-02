from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack to store (start_index, height) pairs
        # This helps us track potential rectangle starting positions
        stack = []
        max_rectangle_area = 0
        
        # Process each bar in the histogram
        for current_index, current_height in enumerate(heights):
            
            # For the first bar, simply add it to stack
            if current_index == 0:
                stack.append((current_index, current_height))
                continue
            
            # If current height equals the last height in stack, skip
            # (no need to add duplicate heights)
            if stack[-1][1] == current_height:
                continue
            
            # If current height is greater, we can extend rectangles
            if stack[-1][1] < current_height:
                stack.append((current_index, current_height))
                continue
            
            # Current height is smaller - we need to calculate areas
            # and pop taller bars from stack
            rectangle_start_index = current_index
            while len(stack) and stack[-1][1] > current_height:
                # Get the position where this rectangle could have started
                rectangle_start_index = stack[-1][0]
                # Calculate area: height * width
                # Width = current_index - start_index of the rectangle
                area = stack[-1][1] * (current_index - stack[-1][0])
                max_rectangle_area = max(max_rectangle_area, area)
                stack.pop()
                
            # Add current bar with the earliest possible start position
            stack.append((rectangle_start_index, current_height))
        
        # Process remaining bars in stack (they extend to the end)
        total_length = len(heights)
        for start_index, bar_height in stack:
            # These rectangles extend from their start to the end of array
            area = bar_height * (total_length - start_index)
            max_rectangle_area = max(max_rectangle_area, area)
            
        return max_rectangle_area


# Test cases
solution = Solution()

# Test case 1: Example from problem
test1 = [2, 1, 5, 6, 2, 3]
result1 = solution.largestRectangleArea(test1)
print(f"Test 1: {test1}")
print(f"Expected: 10, Got: {result1}\n")

# Test case 2: Single bar
test2 = [2, 4]
result2 = solution.largestRectangleArea(test2)
print(f"Test 2: {test2}")
print(f"Expected: 4, Got: {result2}")

"""
Time Complexity: O(n)
- We traverse the heights array once: O(n)
- Each element is pushed and popped from the stack at most once: O(n) total operations
- Final stack processing: O(n) in worst case
- Overall: O(n)

Space Complexity: O(n)
- Stack can contain at most n elements in worst case (when heights are in ascending order)
- No other significant space usage
- Overall: O(n)

Algorithm Explanation:
This solution uses a monotonic stack approach to efficiently find the largest rectangle:

1. We maintain a stack of (index, height) pairs where heights are in ascending order
2. For each bar, we handle three cases:
   - If it's taller than the previous: extend possible rectangles
   - If it's the same height: skip (no new rectangles possible)
   - If it's shorter: calculate areas of rectangles that must end here

3. When we encounter a shorter bar, we pop taller bars and calculate their maximum
   possible rectangle areas. The key insight is that when we pop a bar, we know
   its rectangle cannot extend further right, so we calculate its area.

4. We track the leftmost position each height could start from, allowing us to
   calculate maximum width for each rectangle.

5. After processing all bars, remaining bars in the stack can extend to the end
   of the array, so we calculate their areas.

Key Insight: Each bar determines the height of rectangles, and we use the stack
to efficiently find the maximum width each height can achieve.
"""