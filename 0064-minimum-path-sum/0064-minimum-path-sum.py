class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        dp = [[float('inf')]*(cols+1) for _ in range(rows+1)]
        dp[1][1] = grid[0][0]
        for r in range(1 , rows+1) : 
            for c in range(1 , cols+1) : 
                if r == c == 1 : continue 
                dp[r][c] = min(dp[r-1][c] , dp[r][c-1]) + grid[r-1][c-1]
        return dp[rows][cols]