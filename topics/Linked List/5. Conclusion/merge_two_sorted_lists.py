# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize new LL
        sentinel_head = ListNode(0)
        
        prev_node = sentinel_head
        
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                prev_node.next = list1
                list1 = list1.next
            else:
                prev_node.next = list2
                list2 = list2.next
            
            prev_node = prev_node.next
        
        if list1 == None:
            prev_node.next = list2
        else:
            prev_node.next = list1
        
        return sentinel_head.next