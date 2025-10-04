class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def explore(i , total) : 
            # base cases 
            if i == len(nums) : 
                return 1 if total == target else 0

            return explore(i+1 , total + nums[i]) + explore(i+1 , total - nums[i])

        return explore(0 , 0)