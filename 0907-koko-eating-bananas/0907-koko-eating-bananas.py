import math

def totalTimePerRate(rate , pile ) : 
    total_time = 0
    
    for i in range(len(pile)) : 
        total_time += math.ceil(pile[i] / rate)

    return total_time
    

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1 , max(piles)

        while low < high : 
            mid = ((low+high)//2)
            if totalTimePerRate(mid , piles[:]) > h : 
                low = mid +1 
            elif totalTimePerRate(mid , piles[:]) <= h :
                high = mid 
        return low