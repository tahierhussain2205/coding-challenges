from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Track previous and current nodes in list1, and current node in list2
        prev_node, current_list1 = None, list1
        current_list2 = list2
        head = list1

        while current_list1 or current_list2:
            # If list1 is exhausted, attach remaining list2 nodes
            if not current_list1:
                if prev_node:
                    prev_node.next = current_list2
                    return head
                else:
                    return current_list2

            # If list2 is exhausted, list1 is already connected
            if not current_list2:
                return head

            # Insert list2 node before current_list1 node if smaller
            if current_list1.val >= current_list2.val:
                next_list2_node = current_list2.next
                if prev_node:
                    prev_node.next = current_list2
                    prev_node = prev_node.next
                    prev_node.next = current_list1
                else:
                    prev_node = current_list2
                    prev_node.next = current_list1
                    head = prev_node

                current_list2 = next_list2_node
            else:
                # Move forward in list1
                prev_node = current_list1
                current_list1 = current_list1.next

        return head


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


solution = Solution()

# Test case 1: Both lists have overlapping values
head1 = create_linked_list([1, 2, 4])
head2 = create_linked_list([1, 3, 4])
merged = solution.mergeTwoLists(head1, head2)
print(linked_list_to_array(merged))  # Expected: [1, 1, 2, 3, 4, 4]

# Test case 2: One list is empty
head1 = create_linked_list([])
head2 = create_linked_list([1, 2])
merged = solution.mergeTwoLists(head1, head2)
print(linked_list_to_array(merged))  # Expected: [1, 2]

# Time Complexity: O(n + m) where n and m are the lengths of list1 and list2
# - We iterate through both lists exactly once, visiting each node once
#
# Space Complexity: O(1)
# - We only use a constant amount of extra space for pointers (prev_node, current_list1, current_list2)
# - No additional data structures are created; we rearrange existing nodes
#
# Algorithm: In-place merge using pointer manipulation
# - Traverse both lists simultaneously
# - Compare current nodes and insert smaller node from list2 into list1's position
# - Maintain previous pointer to connect nodes correctly
# - Handle edge cases: empty lists, exhausted lists
