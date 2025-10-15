class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        @cache
        def dfs(r , c) : 
            if r not in range(rows) or c not in range(cols) : 
                return float("inf")
            
            if (r , c) == (0 , 0) : 
                return grid[r][c]
            
            return min(dfs(r-1 , c ) , dfs(r , c-1)) + grid[r][c]
        
        return dfs(rows-1 , cols-1 )

