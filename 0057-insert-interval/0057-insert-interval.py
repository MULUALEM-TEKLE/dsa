class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.append(newInterval)
        intervals.sort(key=lambda interval : interval[0])
        res = []

        for i in range(len(intervals)) : 
            # if interval comes before all
            if newInterval[1] < intervals[i][0] : 
                res.append(newInterval)
                return res + intervals[i:]
            # if interval comes after all 
            elif newInterval[0] > intervals[i][1] :
                res.append(intervals[i])
            # if interval overlaps
            else : 
                newInterval = [min(newInterval[0] , intervals[i][0]) , max(newInterval[1] , intervals[i][1])]
        res.append(newInterval)
        return res 