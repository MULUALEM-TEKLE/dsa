import sys
class Solution:
    def numDecodings(self, s: str) -> int:
        sys.setrecursionlimit(len(s) + 500) # Adjust as needed
        @cache
        def decode(i) : 
            if i == len(s) : 
                return 1 
            if s[i] == '0' : return 0

            res = decode(i+1)
            if i +1 < len(s)and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')) : 
                    res += decode(i+2)
            
            return res 
        
        return decode(0)