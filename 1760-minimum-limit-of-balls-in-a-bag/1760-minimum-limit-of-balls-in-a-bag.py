class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_achieve_penality(targeted_max) : 
            ops_needed = 0 

            for num in nums : 
                ops_needed += (num-1)//targeted_max
            
            return ops_needed <= maxOperations
        

        low = 1 
        high = max(nums)
        res = high

        while low <= high : 
            mid = (low+high)//2

            if can_achieve_penality(mid) : 
                res = mid 
                high = mid-1

            else : 
                low = mid + 1 


        return res 