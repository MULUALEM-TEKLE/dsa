class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows , cols = m , n
        memo = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(r , c , memo ) : 
            if r not in range(rows) or c not in range(cols) : 
                return 0
            if memo[r][c] > 0 : 
                return memo[r][c]
            if r == rows-1 and c == cols-1 : 
                return 1
            memo[r][c] =  dfs(r+1 , c , memo) + dfs(r , c+1 , memo)
            return memo[r][c]
        return dfs(0 , 0 , memo)