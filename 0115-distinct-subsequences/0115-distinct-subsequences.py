class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m , n = len(s) , len(t)
        @cache
        def explore(i , j ) : 
            if j == n : 
                return 1 
            if i == m  : 
                return 0
            ways = 0 
            if  s[i] == t[j] : 
                ways += explore(i+1 , j+1 )
                ways += explore(i+1 , j)
            else :
                ways += explore(i+1 , j)
            return ways
        
        return explore(0 , 0 )
