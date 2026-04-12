class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k > sum(candies) : return 0
        low , high = 1 , max(candies)
        res = low 

        def can_do(amount) : 
            count = 0 
            for candy in candies : 
                count += candy // amount 
            
            return count >= k

        while low <= high : 
            mid = (low+high)//2

            if can_do(mid) : 
                res = mid
                low = mid + 1 
            else : 
                high = mid - 1
        
        return res 
             