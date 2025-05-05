class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == ""  : return True
        if t == "" : return False

        last_pos = 0
        similar_count = 0
        for i in range(len(s)):
            if s[i] in t :
                last_pos = t.index(s[i])
                similar_count += 1
                t = t[last_pos+1 : ]
                continue
            else : 
                return False

        return similar_count  == len(s)


        


       