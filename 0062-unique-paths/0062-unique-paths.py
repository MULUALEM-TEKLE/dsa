class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows , cols = m , n 

        dp = [[0] * (cols) for _ in range(rows)]

        for r in range(rows) : 
            dp[r][0] = 1

        for c in range(cols) : 
            dp[0][c] = 1 
        
        for r in range(1 , rows) : 
            for c in range(1 , cols) : 
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[rows-1][cols-1]