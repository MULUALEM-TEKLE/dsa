class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 : return 
        if n == 1 : return nums[0]
        if n == 2 : return max(nums[0] , nums[1])
        dp = [nums[0] , max(nums[0] , nums[1])]
        for i in range(2 , n-1) : 
            dp[0] , dp[1] = dp[1] , max(dp[1] , nums[i] + dp[0])
        dpp = [nums[1] , max(nums[1] , nums[2])]
        for i in range(3 , n) : 
            dpp[0] , dpp[1] = dpp[1] , max(dpp[1] , nums[i] + dpp[0])
        return max(dp[1] , dpp[1])