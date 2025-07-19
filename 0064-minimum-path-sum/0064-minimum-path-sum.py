class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        visited = set()
        memo = {}
        def dfs(r , c) : 
            if (r , c) in memo : return memo[(r , c)]
            if r not in range(rows) or c not in range(cols) or (r , c) in visited : 
                return float('inf')
            
            if r == rows-1 and c == cols-1 : 
                return grid[r][c]

            visited.add((r , c))
            res = min(dfs(r+1 , c ) , dfs(r , c+1)) + grid[r][c]
            visited.remove((r , c))

            memo[(r , c)] = res
            return memo[(r , c)]

        return  dfs(0 , 0) 