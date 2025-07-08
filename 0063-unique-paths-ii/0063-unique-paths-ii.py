class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        rows , cols = len(grid) , len(grid[0])
        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == 1 : 
                    grid[r][c] = -1
        memo = [[0 for _ in range(cols)] for _ in range(rows)]
        def dfs(r , c , memo) : 
            if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 : 
                return 0
            if memo[r][c] > 0 : 
                return memo[r][c]
            if r == rows-1 and c == cols-1: 
                return 1 
            memo[r][c] = dfs(r+1 , c , memo) + dfs(r , c+1 , memo)
            return memo[r][c]
        return dfs(0 , 0 , memo)