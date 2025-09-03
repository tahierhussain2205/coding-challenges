class MyStack:

    def __init__(self):
        # Using a single list as queue (append to back, pop from front)
        self.queue = []

    def push(self, element: int) -> None:
        # Add element to the back of queue
        self.queue.append(element)

    def pop(self) -> int:
        # Remove and return the last element (LIFO behavior)
        return self.queue.pop()

    def top(self) -> int:
        # Return the last element without removing it
        return self.queue[-1]

    def empty(self) -> bool:
        # Check if queue is empty
        return len(self.queue) == 0


# Test Case 1: Basic stack operations
stack1 = MyStack()

stack1.push(1)
stack1.push(2)

top_result = stack1.top()
pop_result = stack1.pop()
is_empty = stack1.empty()

print("Test Case 1: Basic Operations")
print(f"After push(1), push(2):")
print(f"top() = {top_result}, expected: 2")
print(f"pop() = {pop_result}, expected: 2")
print(f"empty() = {is_empty}, expected: False")
print()

# Test Case 2: Empty stack behavior
stack2 = MyStack()

stack2.push(5)
stack2.pop()
is_empty_after_pop = stack2.empty()

print("Test Case 2: Empty Stack")
print(f"After push(5) then pop():")
print(f"empty() = {is_empty_after_pop}, expected: True")


"""
COMPLEXITY ANALYSIS:

Time Complexity:
- push(): O(1) - Append to end of list
- pop(): O(1) - Remove from end of list  
- top(): O(1) - Access last element
- empty(): O(1) - Check list length

Space Complexity: O(n)
- n = number of elements in the stack
- Single list stores all stack elements

ALGORITHM WALKTHROUGH:
This solution uses a simple list to simulate both queue and stack operations:

1. PUSH: Add element to the end of the list (append operation)
2. POP: Remove element from the end of the list (LIFO behavior)
3. TOP: Access the last element without removing it
4. EMPTY: Check if the list has zero elements
"""
