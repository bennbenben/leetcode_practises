# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel_head = ListNode(0, head)
        prev_node, curr_node = sentinel_head, head
        
        while curr_node and curr_node.next:
            # save pointers
            second = curr_node.next
            third = curr_node.next.next
            
            # make reversal
            second.next = curr_node
            curr_node.next = third
            prev_node.next = second
            
            # update pointers
            prev_node = curr_node
            curr_node = third
        
        return sentinel_head.next