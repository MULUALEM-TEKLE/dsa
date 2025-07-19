class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        dp = [[float('inf')] * (cols+1) for _ in range(rows+1)]
        dp[1][1] = grid[0][0]

        for row in range(1 , rows+1) : 
            for col in range(1 , cols+1) : 
                if row == col == 1 : continue
                dp[row][col] = min(dp[row-1][col] , dp[row][col-1]) + grid[row-1][col-1]
        
        return dp[rows][cols]