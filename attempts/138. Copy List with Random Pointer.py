"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_mapping = {None: None}
        old_head = head
        
        # Populate the hashmap to map old nodes to new nodes
        while old_head:
            node_mapping[old_head] = Node(old_head.val)
            old_head = old_head.next
        
        # Assign pointers for all the new nodes using the hash map
        old_node = head
        while old_node:
            new_node = node_mapping[old_node]
            new_node.next = node_mapping[old_node.next]
            new_node.random = node_mapping[old_node.random]
            old_node = old_node.next
        return node_mapping[head]