class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.count >= self.size:
            return False

        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        self.head = self.head.next
        self.count-=1
        return True
        

    def Front(self) -> int:
        if self.count ==0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.count ==0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.count == self.size:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
#obj = MyCircularQueue()
#param_1 = obj.enQueue()
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
