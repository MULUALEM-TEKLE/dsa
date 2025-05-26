import math

    

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1 , max(piles)

        def totalTimePerRate(rate  ) : 
            total_time = 0
            
            for i in range(len(piles)) : 
                total_time += math.ceil(piles[i] / rate)

            return total_time

        while low < high : 
            mid = ((low+high)//2)
            if totalTimePerRate(mid ) > h : 
                low = mid +1 
            elif totalTimePerRate(mid ) <= h :
                high = mid 
        return low