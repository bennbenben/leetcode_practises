# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:    
        # initialize new LL
        sentinel_head = ListNode(0)
        prev = sentinel_head
        
        # inititalize carry value
        carry = 0
        
        # begin iteration
        while l1 != None or l2 != None or carry != 0:
            # check if any are none
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
            
            # append to the LL
            remainder = (l1.val+l2.val+carry)%10
            carry = (l1.val+l2.val+carry)//10
            prev.next = ListNode(remainder)
            
            # step forward
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
        
        return sentinel_head.next
