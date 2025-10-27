class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m , n = len(word1) , len(word2)
        @cache
        def convert(i , j) : 
            # base cases 
            if i >= m : 
                return n - j
            if j >= n :
                return m - i
            
            if word1[i] == word2[j] : 
                return convert(i+1 , j+1)
            else :
                return 1 + min(convert(i , j+1) , convert(i+1 , j) , convert(i+1 , j+1))
        
        return convert(0 , 0)