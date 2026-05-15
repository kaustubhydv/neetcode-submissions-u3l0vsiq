class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr)%2 == 0:
            val = len(self.arr)//2
            return (self.arr[val] + self.arr[val-1])/2
        else:
            return self.arr[len(self.arr)//2]
        
        