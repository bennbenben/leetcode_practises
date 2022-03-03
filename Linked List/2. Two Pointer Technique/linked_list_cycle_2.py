# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Solution 1: hash map

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes=set()
        while head != None:

            if head in visited_nodes:
                return head
            else:
                visited_nodes.add(head)
                head = head.next

        return None

## Solution 2: two pointer
class Solution:
    def getIntersect(self, head):
        tortise = hare = head

        # A fast pointer will either: Loop around a cycle and meet the slow pointer,
        # or reach the null end of the non-cyclic list
        while hare != None and hare.next != None:
            tortise = tortise.next
            hare = hare.next.next
            if tortise == hare:
                return tortise
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        # If there is a cycle, the fast and slow pointers will intersect at some node
        # Otherwise, there is no cycle -> got no entrance to a cycle
        intersect = self.getIntersect(head)
        if intersect == None:
            return None

        # To find the entrance to the cycle, traverse 2 pointers at the same speed
        # one from the front of the linked list, another from the point of intersection
        tortise = head
        hare = intersect

        while tortise != hare:
            tortise=tortise.next
            hare = hare.next
        return hare