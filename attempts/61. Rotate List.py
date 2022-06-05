# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge cases
        if not head:
            return head
        
        # normalize k to be less than size of linked list
        size = 1
        curr_node = head
        while curr_node.next:
            size += 1
            curr_node = curr_node.next
        k=k%size
        if k==0:
            return head
        
        # get key variables for linked list
        old_tail = curr_node
        
        new_tail = head
        for _ in range(size-k-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # perform pointer updates
        old_tail.next = head
        new_tail.next = None
        
        return new_head