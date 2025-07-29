class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        slen = len(s)
        rep = s[:slen]
        for i in range(slen//2) : 
            if slen % (i+1) == 0 and rep[:i+1] * (slen // (i+1)) == s: 
                    return True 
        return False