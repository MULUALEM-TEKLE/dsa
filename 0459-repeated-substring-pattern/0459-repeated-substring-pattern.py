class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rep = ''
        slen = len(s)
        for i in range(slen//2) : 
            rep += s[i]
            if slen % (i+1) == 0 and rep * (slen // (i+1)) == s: 
                    return True 
        return False