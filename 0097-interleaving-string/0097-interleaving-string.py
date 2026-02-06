class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m , n = len(s1) , len(s2)

        if m+n != len(s3) : 
            return False

        @cache
        def explore(i , j) : 
            if i == m and j == n : 
                return True

            k = i+j

            if (i < m and s1[i] == s3[k] and explore(i+1 , j)) or (j < n and s2[j] == s3[k] and explore(i , j+1)) : 
                return True 
            
            return False
        
        return explore(0 , 0)