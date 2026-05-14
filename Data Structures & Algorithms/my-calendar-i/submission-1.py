class MyCalendar:
    
    def __init__(self):
        self.time = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        for val in self.time:
            if startTime < val[1] and endTime > val[0]:
                return False
        self.time.append([startTime, endTime])
        return True