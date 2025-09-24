class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        started = False 
        counter = 0
        for i in range(len(s)-1 , -1 , -1) : 
            c = s[i]
            if c == " " and not started : 
                continue 
            elif c == " " and started :
                return counter
            elif c != " ": 
                if not started : 
                    started = True 
                counter += 1 
        return counter
            
            