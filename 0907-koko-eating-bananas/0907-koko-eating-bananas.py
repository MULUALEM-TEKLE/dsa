class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1 , max(piles)
        res = max(piles)

        def check(rate) : 
            total_hours = 0
            for pile in piles : 
                total_hours += math.ceil(pile/rate)
            return total_hours


        while low <= high : 
            rate = (low+high)//2 

            if check(rate) > h : 
                low = rate + 1
            elif check(rate) <= h : 
                high = rate - 1
                res = rate
        
        return res
        
