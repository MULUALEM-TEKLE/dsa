class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[1][1] = 1 

        for r in range(1 , len(dp)) : 
            for c in range(1 , len(dp[0])) : 
                if r == c == 1 : continue
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m][n]