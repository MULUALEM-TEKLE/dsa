class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rep = ""
        for i in range(len(s)//2) : 
            rep += s[i]

            if len(s) % len(rep) == 0 : 
                if rep * (len(s)//len(rep)) == s : 
                    return True
        return False 