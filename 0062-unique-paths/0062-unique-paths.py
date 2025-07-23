class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows , cols = m , n
        visited = set() 
        @cache
        def dfs(r , c) : 
            if r not in range(rows) or c not in range(cols) or (r , c) in visited : 
                return 0 
            
            if r == rows-1 and c == cols-1 : 
                return 1 

            visited.add((r , c))
            res = dfs(r+1 , c) + dfs(r , c+1)
            visited.remove((r , c))
            return res 
        
        return dfs(0 , 0)