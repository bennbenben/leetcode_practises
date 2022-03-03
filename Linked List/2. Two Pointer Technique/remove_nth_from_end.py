# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Using for loop

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)

        left_node = dummy_node
        right_node = head

        for _ in range(n):
            right_node = right_node.next

        while right_node != None:
            left_node = left_node.next
            right_node = right_node.next

        left_node.next = left_node.next.next

        return dummy_node.next

# Using while loop (a bit more comprehensive)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)

        left_node = dummy_node
        right_node = head

        while n>0 and right_node != None:
            right_node=right_node.next
            n-=1

        while right_node != None:
            left_node = left_node.next
            right_node = right_node.next

        left_node.next = left_node.next.next

        return dummy_node.next