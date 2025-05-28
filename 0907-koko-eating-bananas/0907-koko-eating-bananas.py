class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def total_hour_to_finish(rate) : 
            total = 0
            for pile in piles : 
                total += math.ceil(pile/rate)
            return total
        
        low , high = 1 , max(piles)

        while low < high : 
            mid = low + (high - low)//2

            if total_hour_to_finish(mid) > h :
                low = mid + 1 
            elif total_hour_to_finish(mid) <= h : 
                high = mid
            else : 
                return mid 

        return high
        