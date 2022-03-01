class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked-list
        If index is invalid, return -1
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        # if index is valid
        current_node = self.head
        for i in range(index+1):
            current_node = current_node.next
        return current_node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list
        After insertion, the new node will be the head of the linked list
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list
        """
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list
        If index equals to length of the linked list, the node will be appended to end of the
        linked list
        If index is > than the length, then the node will not be inserted
        """
        if index > self.size:
            return

        # if index is negative, node will be inserted to the head of the list [weird but ok]
        if index < 0:
            index = 0
        self.size+=1

        # find the predecessor of the node to be added
        pred = self.head
        for i in range(index):
            pred = pred.next

        # initialize the node to be added
        to_add = ListNode(val)
        # insertion
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked-list, given the index is valid
        """
        # if the index is not valid, do nothing
        if index < 0 or index >= self.size:
            return

        # find the predecessor of node to be deleted
        pred = self.head
        for i in range(index):
            pred = pred.next
        self.size-=1

        pred.next = pred.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
