#using python data structure ordered dict
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            x, y = key, self.cache[key]
            self.cache.pop(key)
            self.cache[x] = y
            return y
            
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache.pop(key)
        self.cache[key] = value
        
        if len(self.cache)>self.capacity:
            for key in self.cache.keys():
                self.cache.pop(key)
                break

        ## can also use the following code instead of above paragraph
        # if len(self.cache)>self.capacity:
        #     self.cache.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#using doubly linked list and hashmap
class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev, self.next = None, None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left_node, self.right_node = Node(0,0), Node(0,0)
        self.left_node.next, self.right_node.prev = self.right_node, self.left_node
    
    def remove_Node(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
        
    def insert_Node(self, node):
        prev_node, next_node = self.right_node.prev, self.right_node
        prev_node.next = next_node.prev = node
        node.next, node.prev = next_node, prev_node

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.remove_Node(self.cache[key])
            self.insert_Node(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.remove_Node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_Node(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru_value = self.left_node.next
            print(lru_value.key)
            self.remove_Node(lru_value)
            del self.cache[lru_value.key]
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)