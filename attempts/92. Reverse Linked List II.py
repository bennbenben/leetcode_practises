# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        sentinel_head = ListNode(0, head)
        
        # 1. reach the node at position "left"
        left_prev = sentinel_head
        curr_node = head
        
        for _ in range(left-1):
            left_prev = curr_node
            curr_node = curr_node.next
        
        # 2. reverse from left to right
        prev_node = None
        for _ in range(right-left+1):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node, curr_node = curr_node, next_node
        
        # 3. update pointers: re-assign left and right sides of reversed parts
        left_prev.next.next = curr_node # curr_node is node after "right" node
        left_prev.next = prev_node # pev_node is "right"
        
        return sentinel_head.next