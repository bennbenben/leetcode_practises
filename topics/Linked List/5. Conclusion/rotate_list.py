# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head

        size = 1
        tail = head
        while tail.next != None:
            tail = tail.next
            size += 1

        k = k%size
        if k == 0:
            return head

        curr_node = head
        for _ in range(size-k-1):
            curr_node = curr_node.next

        new_head = curr_node.next
        curr_node.next = None
        tail.next = head

        return new_head