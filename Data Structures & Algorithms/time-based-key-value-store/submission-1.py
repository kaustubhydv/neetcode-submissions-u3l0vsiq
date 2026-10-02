class TimeMap:

    def __init__(self):
        self.users = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.users:
            self.users[key] = {}
        self.users[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.users:
            return ""
        if timestamp in self.users[key]:
            return self.users[key][timestamp]
        else:
            t = float('-inf')
            for k in self.users[key].keys():
                if k < timestamp:
                    t = max(t, k)
            return self.users[key][t] if t != float('-inf') else ""

            
            
                
        
