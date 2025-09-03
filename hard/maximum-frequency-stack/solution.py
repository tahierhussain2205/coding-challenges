class FreqStack:
    """
    A stack-like data structure that pops elements based on frequency.
    Most frequent elements are popped first, with ties broken by recency (stack order).

    Uses a combination of frequency tracking and a stack with frequency annotations
    to efficiently maintain and retrieve the most frequent element.
    """

    def __init__(self):
        # Maps each value to its current frequency count
        self.frequency_map = {}
        # Stack storing (value, frequency_at_push_time) tuples
        self.element_stack = []

    def push(self, val: int) -> None:
        """
        Push a value onto the frequency stack.

        Algorithm:
        1. Increment the frequency count for this value
        2. Push (value, current_frequency) tuple onto the stack

        The frequency stored with each element represents how many times
        that value had been seen when it was pushed.
        """
        # Update frequency count for this value
        self.frequency_map[val] = self.frequency_map.get(val, 0) + 1
        # Store the element with its frequency at push time
        self.element_stack.append((val, self.frequency_map[val]))

    def pop(self) -> int:
        """
        Remove and return the most frequent element from the stack.
        If there's a tie, return the element closest to the top of the stack.

        Algorithm:
        1. Find the maximum frequency among all elements
        2. Scan from top of stack to find the first element with max frequency
        3. Remove that element and decrement its frequency count
        4. Return the removed element
        """
        # Find the highest frequency currently in the stack
        max_frequency = max(self.frequency_map.values())

        # Start from the top of the stack (most recent)
        stack_index = len(self.element_stack) - 1

        # Find the most recent element with maximum frequency
        while self.element_stack[stack_index][1] != max_frequency:
            stack_index -= 1

        # Get the element to remove
        element_to_remove = self.element_stack[stack_index][0]
        # Decrement its frequency count
        self.frequency_map[element_to_remove] -= 1
        # Remove it from the stack
        del self.element_stack[stack_index]

        return element_to_remove


# Test Case 1: Example from problem description
print("=== Test Case 1: Problem Example ===")
freq_stack = FreqStack()

# Push sequence: [5, 7, 5, 7, 4, 5]
operations = [5, 7, 5, 7, 4, 5]
for val in operations:
    freq_stack.push(val)
    print(f"Pushed {val}")

# Pop sequence should return: [5, 7, 5, 4]
expected_pops = [5, 7, 5, 4]
actual_pops = []

for i in range(4):
    popped = freq_stack.pop()
    actual_pops.append(popped)
    print(f"Popped: {popped}")

print(f"Expected: {expected_pops}")
print(f"Actual: {actual_pops}")
print(f"Test 1 Passed: {actual_pops == expected_pops}")
print()

# Test Case 2: Multiple elements with same frequency
print("=== Test Case 2: Tie-breaking Test ===")
freq_stack2 = FreqStack()

# Push: [1, 2, 3] - all have frequency 1
# Pop should return 3 (most recent)
freq_stack2.push(1)
freq_stack2.push(2)
freq_stack2.push(3)
print("Pushed: 1, 2, 3")

result = freq_stack2.pop()
print(f"Popped: {result}")
print(f"Expected: 3 (most recent with freq 1)")
print(f"Test 2 Passed: {result == 3}")
print()

# Additional verification
result2 = freq_stack2.pop()
print(f"Next pop: {result2}")
print(f"Expected: 2 (next most recent)")
print(f"Verification Passed: {result2 == 2}")

"""
COMPLEXITY ANALYSIS:

Time Complexity:
- push(): O(1) - Constant time to update frequency map and append to stack
- pop(): O(n) - Need to find max frequency O(n), then scan stack O(n) in worst case
  where n is the number of elements currently in the stack

Space Complexity: O(n)
- frequency_map: O(k) where k is number of unique values
- element_stack: O(n) where n is total number of elements pushed
- Overall: O(n) since n >= k

ALGORITHM WALKTHROUGH:
This solution uses a frequency tracking approach with annotated stack elements:

1. PUSH Operation:
   - Update frequency count for the value
   - Store (value, frequency_at_push_time) tuple in stack
   - This preserves the frequency context when each element was added

2. POP Operation:
   - Find maximum frequency among all current elements
   - Scan stack from top (most recent) to find first element with max frequency
   - This naturally handles tie-breaking by recency (LIFO order)
   - Remove element and decrement its frequency

KEY INSIGHTS:
- Each stack element stores its frequency at push time
- This allows us to identify which elements currently have the maximum frequency
- Scanning from top ensures most recent element wins ties
- Frequency map tracks current state, while stack preserves historical context

FUTURE OPTIMIZATION:
- Current approach has O(n) pop due to max() and linear search
- Could optimize to O(log n) using heap + frequency buckets approach
- Trade-off: Current solution is simpler and more intuitive to understand
"""
