class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        alt = ""
        rem = ""

        m , n = len(word1) , len(word2)

        if m > n : 
            rem = word1[n :]
            l = n
        else : 
            rem = word2[m:]
            l = m
        
        for i in range(l) : 
            alt += word1[i]
            alt += word2[i]
        
        return alt + rem 