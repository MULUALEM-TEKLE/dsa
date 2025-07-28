class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        dp = [[float('inf')]*(cols+1) for _ in range(rows+1)]
        dp[1][1] = grid[0][0]

        for r in range(1 , len(dp)) : 
            for c in range(1 , len(dp[0])) : 
                if r == c == 1 : continue 
                dp[r][c] = grid[r-1][c-1] + min(dp[r-1][c] , dp[r][c-1])
        
        return dp[rows][cols]