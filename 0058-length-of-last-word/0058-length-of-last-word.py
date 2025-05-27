class Solution:
    def lengthOfLastWord(self, s: str) -> int:  
        counter = 0 
        for i in range(len(s)-1 , -1 , -1 ) : 
            if s[i] == " " and counter :
                return counter 
            elif s[i] != " " :
                counter += 1  

        return counter

       