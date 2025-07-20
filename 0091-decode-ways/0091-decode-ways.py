class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def decode(i) : 
            if i >= len(s) : return 1
            if s[i] == '0' : return 0

            res = decode(i+1)
            if i < len(s) - 1 : 
                if s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456') : 
                    res += decode(i+2)
            return res
        
        return decode(0)