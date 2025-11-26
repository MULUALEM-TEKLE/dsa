class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        INF = 100000
        memo = [[-1]*(target+1) for _ in range(len(nums)+1)]
        def dfs(i , x ) : 
            if x == target : 
                return 0
            if i == len(nums) or x > target : 
                return -INF
            if memo[i][x] != -1 : 
                return memo[i][x]

            memo[i][x] = max(1+dfs(i+1 , x+nums[i]) , dfs(i+1 , x))
            return memo[i][x]
        
        res = dfs(0 , 0)
        if res < 0 : 
            return -1
        return res