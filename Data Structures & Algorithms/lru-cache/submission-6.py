class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.leastUsed = []
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.leastUsed.remove(key)
            self.leastUsed.append(key)
            return self.cache[key] 
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and self.capacity == len(self.cache):
            self.cache.pop(self.leastUsed.pop(0))
        if key not in self.cache:
            self.leastUsed.append(key)
        else:
            self.leastUsed.remove(key)
            self.leastUsed.append(key)
        self.cache[key] = value

        
