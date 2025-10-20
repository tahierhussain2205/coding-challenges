from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Track visited nodes using a set to detect cycles
        visited_nodes = set()
        current_node = head

        while current_node:
            # If we've seen this node before, we found a cycle
            if current_node in visited_nodes:
                return True

            # Mark current node as visited and move to next
            visited_nodes.add(current_node)
            current_node = current_node.next

        # Reached end of list without finding a cycle
        return False


# Helper function to create linked list with cycle
def create_linked_list_with_cycle(values, index):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)

    # Create cycle if index is valid
    if index != -1:
        current.next = nodes[index]

    return head


# Test Case 1: List with cycle
head1 = create_linked_list_with_cycle([1, 2, 3, 4], 1)
print(Solution().hasCycle(head1))  # Expected: True

# Test Case 2: List without cycle
head2 = create_linked_list_with_cycle([1, 2], -1)
print(Solution().hasCycle(head2))  # Expected: False


"""
Time Complexity: O(n)
- We visit each node at most once before detecting a cycle or reaching the end
- Set operations (add, lookup) are O(1) on average

Space Complexity: O(n)
- In the worst case (no cycle), we store all n nodes in the visited_nodes set

Algorithm Explanation:
This solution uses a hash set to track visited nodes. As we traverse the linked list,
we check if the current node exists in our set. If it does, we've found a cycle.
If we reach the end of the list (None), there's no cycle.

Note: An alternative O(1) space solution exists using Floyd's Cycle Detection Algorithm
(slow and fast pointers), but this hash set approach is more intuitive.
"""
