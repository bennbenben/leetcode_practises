# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_1, list_2 = list(), list()
        
        while l1:
            list_1.append(str(l1.val))
            l1 = l1.next
        while l2:
            list_2.append(str(l2.val))
            l2 = l2.next
        
        val_1, val_2 = int("".join(list_1)), int("".join(list_2))
        output_list = list(str(val_1+val_2))

        sentinel_head = ListNode(0)
        prev_node = sentinel_head
        for head in output_list:
            new_node = ListNode(int(head))
            prev_node.next = new_node
            prev_node = new_node
        
        return sentinel_head.next