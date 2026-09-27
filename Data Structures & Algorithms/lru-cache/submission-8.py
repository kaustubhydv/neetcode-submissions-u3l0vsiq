class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.right.prev, self.left.next = self.left, self.right
        self.cap = capacity

    def insert(self, node):
        node.prev, node.next = self.right.prev, self.right
        self.right.prev.next, self.right.prev = node, node

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        else:
            if len(self.cache) == self.cap:
                lru = self.left.next
                self.remove(lru)
                self.cache.pop(lru.key)
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
            
        
