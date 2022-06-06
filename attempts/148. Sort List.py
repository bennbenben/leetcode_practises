# using standard iterations
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        node_vals = list()
        
        while curr_node:
            node_vals.append(curr_node.val)
            curr_node = curr_node.next
        
        node_vals.sort()
        sentinel_head = ListNode(0)
        prev_node = sentinel_head
        
        for val in node_vals:
            new_node = ListNode(val)
            prev_node.next = new_node
            prev_node = new_node
        
        return sentinel_head.next

# using priority queue (heap) data structure
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        heap_list = list()
        
        while curr:
            heapq.heappush(heap_list, curr.val)
            curr = curr.next
        
        sentinel_node = ListNode(0)
        prev_node = sentinel_node
        
        while heap_list:
            node_val = heapq.heappop(heap_list)
            new_node = ListNode(node_val)
            prev_node.next = new_node
            prev_node = new_node
        
        return sentinel_node.next