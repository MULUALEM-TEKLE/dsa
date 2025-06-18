class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        visited = set()

        def dfs(r , c) : 
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r , c) in visited : 
                return 0

            visited.add((r, c))
            return grid[r][c] + dfs(r+1 , c) + dfs(r-1 , c)+ dfs(r , c+1)+ dfs(r , c-1)

        max_fishes = 0
        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] != 0 and (r,c) not in visited : 
                    max_fishes = max(max_fishes , dfs(r , c))
        
        return max_fishes