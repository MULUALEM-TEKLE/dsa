class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval : interval[0])
        print(intervals)
        res = []

        for interval in intervals : 
            if not res or res[-1][1] < interval[0] : 
                res.append(interval)
            else : 
                res[-1] = [res[-1][0] , max(res[-1][1] , interval[1])]
        
        return res 