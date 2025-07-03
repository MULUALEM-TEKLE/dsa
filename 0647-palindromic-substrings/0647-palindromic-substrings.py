class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(left , right) : 
            res = 0
            while left >= 0 and right < len(s) and s[left] == s[right] : 
                res += 1 
                left -= 1
                right += 1 
            return res

        counter = 0
        for i in range(len(s)) : 
            counter += check(i , i)
            counter += check(i , i+1)
        return counter 