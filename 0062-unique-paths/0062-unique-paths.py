class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def explore(row , col) : 
            if row >= m or col >= n : 
                return 0

            if row == m-1 and col == n-1 : 
                return 1 
            
            path = 0 
            path += explore(row+1 , col)
            path += explore(row , col+1)

            return path
        
        return explore(0 , 0)