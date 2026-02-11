class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        rows , cols = len(grid) , len(grid[0])
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1 : return 0

        @cache
        def explore(r , c) : 
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 1 : 
                return 0
            if r == rows-1 and c == cols-1 : 
                return 1 
            
            return explore(r+1 , c ) + explore(r , c+1)
        
        return explore(0 , 0)