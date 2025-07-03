class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left , right) : 
            while  left >= 0 and right < len(s) and s[left] == s[right] : 
                left -= 1
                right += 1 
            return s[left+1 : right]

        maxlen = "" 
        for i in range(len(s)) : 
            check = helper(i ,i)
            if len(check) > len(maxlen) : maxlen = check

            check = helper(i ,i+1)
            if len(check) > len(maxlen) : maxlen = check

        return maxlen