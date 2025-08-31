class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows , cols = len(matrix) , len(matrix[0])
        @cache
        def dfs(r , c) : 
            if r not in range(rows) or c not in range(cols) : 
                return float('inf')
            
            if r == rows - 1 : 
                return matrix[r][c] 
            
            return matrix[r][c] + min(dfs(r+1 , c-1) , dfs(r+1 , c) , dfs(r+1 , c+1))

        res = float("inf")
        for c in range(cols) : 
            res = min(res , dfs(0,c))
        
        return res
