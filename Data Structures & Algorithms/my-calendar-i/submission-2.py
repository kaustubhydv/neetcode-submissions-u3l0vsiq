from sortedcontainers import SortedList
class MyCalendar:
    
    def __init__(self):
        self.time = SortedList()
        

    def book(self, startTime: int, endTime: int) -> bool:
        idx = self.time.bisect_left((startTime, endTime))
        if idx > 0 and self.time[idx-1][1] > startTime:
            return False
        if idx < len(self.time) and self.time[idx][0] < endTime:
            return False
        self.time.add((startTime, endTime))
        return True
        