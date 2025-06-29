class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)-1
        dp = [False] * len(nums)
        def dfs(pos) : 
            if dp[pos] : return
            if pos == N : 
                return True 
            cur = nums[pos]
            dp[pos] = True
            for i in range(1 , cur+1) : 
                if dfs(pos + i) : 
                    return True
            return dp[N]
        return dfs(0)