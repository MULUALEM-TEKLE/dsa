class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return True in [(len(s) % (i+1) == 0 and s[:i+1] * (len(s) // (i+1)) == s) for i in range(len(s)//2) ]