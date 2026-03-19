from heapq import heappush , heappop
class MedianFinder:

    def __init__(self):
        self.small_team = []
        self.big_team = []

    def addNum(self, num: int) -> None:
        heappush(self.small_team , -num)
        if (self.small_team and self.big_team and (-self.small_team[0] > self.big_team[0])) : 
            val = -heappop(self.small_team)
            heappush(self.big_team , val)
        
        if len(self.small_team) > len(self.big_team) + 1 : 
            val = -heappop(self.small_team)
            heappush(self.big_team , val)
        elif len(self.big_team) > len(self.small_team) : 
            val = heappop(self.big_team)
            heappush(self.small_team , -val)


    def findMedian(self) -> float:
        if len(self.small_team) > len(self.big_team) : 
            return float(-self.small_team[0])
        else : 
            return float((-self.small_team[0] + self.big_team[0])/2)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()