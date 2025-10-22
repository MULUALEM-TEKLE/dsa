class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def explore(i , cur) : 
            if i == len(nums) : 
                return 1 if cur == target else 0
            return explore(i+1 , cur+nums[i]) + explore(i+1 , cur-nums[i])
        
        return explore(0 , 0)

        # space : dp = [[0]*(target+1) for _ in range(len(nums))]
        # base case : last row : 1 for c == target 
        # recurrence : dp[i-1][c+nums[i]] + dp[i-1][c-nums[i]]

        # dp = [[0]*(target+1) for _ in range(len(nums))]

        # for i in range(len(nums)) : 
        #     for c in range(target+1) : 
        #         plus = dp[i][]