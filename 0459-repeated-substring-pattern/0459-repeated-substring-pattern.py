class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1 , (len(s)//2)+1) : 
            sub = s[:i]
            if len(s) % len(sub) == 0 and (len(s) // len(sub)) * sub == s : 
                return True 
        return False