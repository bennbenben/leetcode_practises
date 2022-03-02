# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Solution 1: hash map

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        while head:
            if head not in visited_nodes:
                visited_nodes.add(head)
                head = head.next
            else:
                return True
        return False

## Another solution: slow/fast pointer

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow_pointer = head
        fast_pointer = head.next

        while slow_pointer != fast_pointer:

            if fast_pointer == None or fast_pointer.next == None:
                return False

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return True
