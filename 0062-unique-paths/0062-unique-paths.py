class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def explore(row , col) : 
            if row >= m or col >= n : 
                return 0

            if row == m-1 and col == n-1 : 
                return 1 
            
            return explore(row+1 , col) + explore(row , col+1)
        
        return explore(0 , 0)