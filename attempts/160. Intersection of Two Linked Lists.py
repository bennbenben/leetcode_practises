# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        
        head_a, head_b = headA, headB
        
        while head_a:
            visited.add(head_a)
            head_a = head_a.next
        
        while head_b:
            if head_b in visited:
                return head_b
            else:
                visited.add(head_b)
            head_b = head_b.next
            
        return None