import math

def totalTimePerRate(rate , pile ) : 
    total_time = 0
    
    for i in range(len(pile)) : 
        total_time += math.ceil(pile[i] / rate)


    return total_time
    

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles) ==  1:
        #     return (piles[0] % h) + 1

        low , high = 1 , max(piles)

        while low <= high : 
            mid = ((low+high)//2)
            print(f"mid is now {mid}")
            if totalTimePerRate(mid , piles[:]) > h : 
                print(f"time per rate is greater than {h}")
                low = mid +1 
                print(f"zooming in to {low} to {high}")
            elif totalTimePerRate(mid , piles[:]) <= h :
                print(f"time per rate is less than {h}")
                high = mid - 1
                print(f"zooming in to {low} to {high}")
            # else : 
            #     return mid
        return low