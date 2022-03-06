"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # if empty list
        if head==None:
            new_node = Node(val=insertVal, next=None)
            new_node.next = new_node
            return new_node

        prev_node = head
        curr_node = head.next

        while True:
            # Case 1: insert in between 2 nodes (excluding the max/min node)
            if prev_node.val <= insertVal <= curr_node.val:
                prev_node.next = Node(insertVal, curr_node)
                return head

            # Case 2: insert between the max/min node
            elif prev_node.val > curr_node.val:
                if insertVal >= prev_node.val or insertVal <= curr_node.val:
                    prev_node.next = Node(insertVal, curr_node)
                    return head

            
            prev_node = curr_node
            curr_node = curr_node.next

            # loop condition
            if prev_node == head:
                break

        # Case 3: did not insert node into the loop - all loop node vals are same
        prev_node.next = Node(insertVal, curr_node)
        return head