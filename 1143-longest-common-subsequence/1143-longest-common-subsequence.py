class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m , n = len(text1) , len(text2)

        @cache
        def explore(i , j) : 
            if i == m or j == n : 
                return 0
            
            res = 0 

            if text1[i] == text2[j] : 
                res = 1 + explore(i+1 , j+1)
            else : 
                res += max(explore(i+1 , j) , explore(i , j+1))
            
            return res 
        
        return explore(0 , 0)