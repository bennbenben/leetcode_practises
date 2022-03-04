# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array_list = list()
        
        while head != None:
            array_list.append(head.val)
            head = head.next
        
        if array_list == array_list[::-1]:
            return True
        else:
            return False