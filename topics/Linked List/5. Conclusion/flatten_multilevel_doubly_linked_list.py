"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return
        
        sentinel_head = Node(0, None, head, None)
        prev = sentinel_head
        
        stack = list()
        stack.append(head)
        
        while len(stack) != 0:
            curr_node = stack.pop()
            
            prev.next = curr_node
            curr_node.prev = prev
            
            if curr_node.next != None:
                stack.append(curr_node.next)
            if curr_node.child != None:
                stack.append(curr_node.child)
                curr_node.child = None # remove child pointers
            
            prev = curr_node
        
        sentinel_head.next.prev = None # remove sentinel head from the result
        return sentinel_head.next
