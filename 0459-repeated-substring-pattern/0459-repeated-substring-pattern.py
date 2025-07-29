class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        slen = len(s)
        return True in [(slen % (i+1) == 0 and s[:i+1] * (slen // (i+1)) == s) for i in range(slen//2) ]
        # for  : 
        #     if : 
        #             return True 
        # return False