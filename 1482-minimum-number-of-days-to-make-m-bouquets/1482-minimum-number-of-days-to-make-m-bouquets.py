class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k : return -1
        low , high = min(bloomDay) , max(bloomDay)
        res = high
        while low <= high : 
            mid = (low+high)//2

            groups = 0
            count = 0
            for bd in bloomDay : 
                if bd <= mid : 
                    count += 1 
                    if count == k : 
                        groups += 1 
                        count = 0 
                else : 
                    count = 0

            if groups >= m : 
                res = mid 
                high = mid - 1 
            else : 
                low = mid + 1 
        return res 