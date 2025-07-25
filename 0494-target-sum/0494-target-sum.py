class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def backtrack(i , total) : 
            if i == len(nums) : 
                return 1 if total == target else 0
            
            return backtrack(i+1 , total + nums[i]) + backtrack(i+1 , total - nums[i])
        
        return backtrack(0 , 0)