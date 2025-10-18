class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def explore(i , cur) : 
            if i == len(nums) : 
                return 1 if cur == target else 0
            
            return explore(i+1 , cur - nums[i]) + explore(i+1 , cur + nums[i])
        
        return explore(0 , 0)