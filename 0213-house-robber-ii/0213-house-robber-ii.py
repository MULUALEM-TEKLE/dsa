class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1 : 
            return nums[0]
        if n == 2 : 
            return max(nums[0] , nums[1])
        
        def steal(sub) : 
            dp = [sub[0] , max(sub[0] , sub[1])]
            for i in range(2 , len(sub)) : 
                dp[0] , dp[1] = dp[1] , max(sub[i] + dp[0] , dp[1])
            return dp[1]
        
        return max(steal(nums[1:]) , steal(nums[:-1]))

