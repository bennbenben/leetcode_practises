# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize sentinel nodes for odd and even
        even_head = ListNode(0)
        odd_head = ListNode(0)

        # Initialize pointers to sentinel nodes
        even_head_ptr = even_head
        odd_head_ptr = odd_head

        # Initialize flag to toggle between odd and even node index
        flag = True # True for node index is odd

        while head != None:
            if flag == True: # node index == odd
                odd_head.next = head
                odd_head = odd_head.next

            else: # node index == even
                even_head.next = head
                even_head = even_head.next

            flag = not flag
            head = head.next

        even_head.next = None # terminate the even linked list
        odd_head.next = even_head_ptr.next # join end of odd -> start of even
        
        return odd_head_ptr.next