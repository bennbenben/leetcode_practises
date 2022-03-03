# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited_nodes_A=set()

        while headA is not None:
            visited_nodes_A.add(headA)
            headA = headA.next

        while headB is not None:
            if headB in visited_nodes_A:
                return headB
            else:
                headB = headB.next
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_A = headA
        node_B = headB

        while node_A != node_B:
            if node_A != None:
                node_A = node_A.next
            else:
                node_A = headB

            if node_B != None:
                node_B = node_B.next
            else:
                node_B = headA
        return node_A