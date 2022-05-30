# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        accumulate_list = list()
        output_list = list()
        for head in lists:
            while head:
                accumulate_list.append(head.val)
                head = head.next
        accumulate_list = sorted(accumulate_list)
        
        sentinel_head = ListNode(0)
        head = sentinel_head
        
        for i in range(len(accumulate_list)):
            head.next = ListNode(accumulate_list[i])
            head = head.next
            
        return sentinel_head.next