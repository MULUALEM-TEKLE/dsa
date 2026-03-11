class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval : interval[1])
        res = 0 
        end = float('-inf')
        for interval in intervals : 
            if interval[1] > end : 
                end = interval[1]
            else : 
                res += 1
      
        return res  