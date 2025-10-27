class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m , n = len(s1) , len(s2)

        if m + n != len(s3) : 
            return False
        @cache
        def explore(i , j) : 
            if i == m and j == n : 
                return True 
            
            k = i+j
            
            take_i = False
            if i < m and s1[i] == s3[k] : 
                take_i = explore(i+1 , j)
            
            take_j = False
            if j < n and s2[j] == s3[k] : 
                take_j = explore(i , j+1)
            
            return take_i or take_j
        
        return explore(0 , 0)