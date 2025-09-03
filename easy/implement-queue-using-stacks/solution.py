class MyQueue:

    def __init__(self):
        # Using a single list as stack (append to end, pop from front for FIFO)
        self.queue_list = []

    def push(self, element: int) -> None:
        # Add element to the back of the queue
        self.queue_list.append(element)

    def pop(self) -> int:
        # Remove and return element from the front of the queue
        return self.queue_list.pop(0)

    def peek(self) -> int:
        # Return the front element without removing it
        return self.queue_list[0]

    def empty(self) -> bool:
        # Check if queue is empty
        return len(self.queue_list) == 0


# Test Case 1: Basic queue operations
queue1 = MyQueue()

queue1.push(1)
queue1.push(2)

peek_result = queue1.peek()
pop_result = queue1.pop()
is_empty = queue1.empty()

print("Test Case 1: Basic Operations")
print(f"After push(1), push(2):")
print(f"peek() = {peek_result}, expected: 1")
print(f"pop() = {pop_result}, expected: 1")
print(f"empty() = {is_empty}, expected: False")
print()

# Test Case 2: Empty queue behavior
queue2 = MyQueue()

queue2.push(3)
queue2.pop()
is_empty_after_pop = queue2.empty()

print("Test Case 2: Empty Queue")
print(f"After push(3) then pop():")
print(f"empty() = {is_empty_after_pop}, expected: True")


"""
COMPLEXITY ANALYSIS:

Time Complexity:
- push(): O(1) - Append to end of list
- pop(): O(n) - Remove from front of list (requires shifting all elements)
- peek(): O(1) - Access first element
- empty(): O(1) - Check list length

Space Complexity: O(n)
- n = number of elements in the queue
- Single list stores all queue elements

ALGORITHM WALKTHROUGH:
This solution uses a single list to simulate queue operations:

1. PUSH: Add element to the end of the list (append operation)
2. POP: Remove element from the front of the list (FIFO behavior)
3. PEEK: Access the first element without removing it
4. EMPTY: Check if the list has zero elements

"""
