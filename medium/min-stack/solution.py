class MinStack:

    def __init__(self):
        # Stack stores tuples: (value, current_minimum_at_this_level)
        self.element_stack = []

    def push(self, val: int) -> None:
        # Determine the minimum value at this stack level
        current_minimum = None
        if len(self.element_stack) == 0:
            # First element - it's the minimum by default
            current_minimum = val
        else:
            # Compare new value with previous minimum
            previous_minimum = self.element_stack[-1][1]
            current_minimum = min(val, previous_minimum)

        # Store both the value and the minimum at this level
        self.element_stack.append((val, current_minimum))

    def pop(self) -> None:
        # Remove the top element (both value and its associated minimum)
        self.element_stack.pop()

    def top(self) -> int:
        # Return the value of the top element (first element of tuple)
        return self.element_stack[-1][0]

    def getMin(self) -> int:
        # Return the minimum at current stack level (second element of tuple)
        return self.element_stack[-1][1]


# Test cases
print("Test case 1:")
min_stack = MinStack()
print("push(-2)")
min_stack.push(-2)
print("push(0)")
min_stack.push(0)
print("push(-3)")
min_stack.push(-3)
print("getMin():", min_stack.getMin())  # Expected: -3
print("pop()")
min_stack.pop()
print("top():", min_stack.top())        # Expected: 0
print("getMin():", min_stack.getMin())  # Expected: -2

print("\nTest case 2:")
min_stack2 = MinStack()
print("push(5)")
min_stack2.push(5)
print("push(1)")
min_stack2.push(1)
print("push(3)")
min_stack2.push(3)
print("getMin():", min_stack2.getMin())  # Expected: 1
print("top():", min_stack2.top())       # Expected: 3
print("pop()")
min_stack2.pop()
print("getMin():", min_stack2.getMin())  # Expected: 1

"""
Time Complexity Analysis:
- push(): O(1) - Appending to list and min comparison are constant time
- pop(): O(1) - Removing from end of list is constant time
- top(): O(1) - Accessing last element is constant time
- getMin(): O(1) - Accessing stored minimum is constant time
- Overall: O(1) for all operations

Space Complexity Analysis:
- O(n) where n is the number of elements in the stack
- Each element stores a tuple (value, minimum), so space usage is 2n
- No additional data structures needed beyond the main stack

Algorithm Explanation:
1. Store each element as a tuple: (value, minimum_at_this_level)
2. When pushing: calculate minimum between new value and previous minimum
3. When popping: remove entire tuple, previous minimum is automatically restored
4. getMin() simply returns the stored minimum from the top tuple
5. This approach ensures O(1) access to minimum without rescanning the stack
"""
