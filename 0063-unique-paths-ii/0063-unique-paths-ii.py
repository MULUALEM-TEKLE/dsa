class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        rows , cols = len(grid) , len(grid[0])
        memo = [[False] * cols for _ in range(rows)]
        visited = set()
        def dfs(r , c):
            if r not in range(rows) or c not in range(cols) or (r , c) in visited or grid[r][c] == 1: 
                return 0
            if memo[r][c] : return memo[r][c]
            if r == rows - 1 and c == cols - 1 : 
                return 1 
            visited.add((r , c))
            res = dfs(r+1 , c) + dfs(r , c+1)
            visited.remove((r , c))
            memo[r][c] = res
            return res
        return dfs(0 , 0)