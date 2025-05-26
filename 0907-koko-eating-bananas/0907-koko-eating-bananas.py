import math

    

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1 , max(piles)

        def totalTimePerRate(rate  ) : 
          

            return sum([math.ceil(pile/rate) for pile in piles])

        while low < high : 
            mid = ((low+high)//2)
            if totalTimePerRate(mid ) > h : 
                low = mid +1 
            elif totalTimePerRate(mid ) <= h :
                high = mid 
        return low