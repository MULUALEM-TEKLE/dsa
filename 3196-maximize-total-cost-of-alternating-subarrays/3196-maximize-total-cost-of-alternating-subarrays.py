from functools import cache
class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def explore(index, can_sub) : 
            if index == n : 
                return 0
            
            res = nums[index] + explore(index+1 , True )

            if can_sub : 
                res = max(res , -nums[index] + explore(index+1 , False))
            
            return res 
        
        return nums[0] + explore(1 , True)
