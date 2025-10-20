from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers for both input lists
        node1 = l1
        node2 = l2

        # Dummy head for result list simplifies insertion logic
        dummy_head = ListNode(0)
        current = dummy_head

        carry = 0

        # Process both lists until both are exhausted
        while node1 or node2:
            # Get current digit values (0 if node is None)
            digit1 = node1.val if node1 else 0
            digit2 = node2.val if node2 else 0

            # Calculate sum of digits plus carry
            total = digit1 + digit2 + carry

            # Extract new carry and digit
            carry = total // 10
            digit = total % 10

            # Add new node to result list
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes if available
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next

        # Handle final carry if present
        if carry:
            current.next = ListNode(carry)

        return dummy_head.next


# Helper function to create linked list from array
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to array for testing


def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test case 1: 342 + 465 = 807
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_array(result))  # Expected: [7, 0, 8]

# Test case 2: 9999999 + 9999 = 10009998
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_array(result))  # Expected: [8, 9, 9, 9, 0, 0, 0, 1]

# Time Complexity: O(max(n, m)) where n and m are lengths of l1 and l2
#   - We iterate through both lists once, processing each node exactly once
#   - The loop continues until both lists are exhausted
#
# Space Complexity: O(max(n, m))
#   - The result linked list will have at most max(n, m) + 1 nodes
#   - No additional data structures used besides the result list
#
# Algorithm: Elementary Math Addition
#   - Simulate digit-by-digit addition from least significant to most significant digit
#   - Track carry between digit positions
#   - Handle lists of different lengths by treating missing nodes as 0
