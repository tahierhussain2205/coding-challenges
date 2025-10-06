from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers: previous node (None) and current node (head)
        previous_node, current_node = None, head

        # Traverse the list and reverse pointers
        while current_node:
            # Store the next node before breaking the link
            next_node = current_node.next
            # Reverse the current node's pointer
            current_node.next = previous_node
            # Move previous and current pointers one step forward
            previous_node = current_node
            current_node = next_node

        # Previous node is now the new head of the reversed list
        return previous_node


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

# Test cases
solution = Solution()

# Test case 1
head1 = create_linked_list([0, 1, 2, 3])
reversed1 = solution.reverseList(head1)
print(linked_list_to_array(reversed1))  # Expected: [3, 2, 1, 0]

# Test case 2
head2 = create_linked_list([])
reversed2 = solution.reverseList(head2)
print(linked_list_to_array(reversed2))  # Expected: []

# Time Complexity: O(n) - where n is the number of nodes in the linked list
#                         We traverse each node exactly once
# Space Complexity: O(1) - Only using a constant amount of extra space (pointers)
#                          No additional data structures needed
#
# Algorithm: Iterative pointer reversal
# 1. Use three pointers: previous (initially None), current (head), and next
# 2. Traverse the list, reversing each node's pointer to point to the previous node
# 3. Move all pointers one step forward until we reach the end
# 4. Return the previous pointer as the new head
