class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)-1
        dp = [None] * len(nums)
        def dfs(pos) : 
            if pos == N : 
                return True 
            if pos > N : 
                return False
            if dp[pos] is not None : return dp[pos]
            cur = nums[pos]
            for i in range(1 , cur+1) : 
                if dfs(pos + i) : 
                    dp[pos] = True
                    return True
            dp[pos] = False
            return False
        return dfs(0)