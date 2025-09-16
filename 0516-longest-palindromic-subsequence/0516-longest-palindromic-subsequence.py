class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_len = len(s)
        rev = s[::-1]

        @cache
        def solve(i , j) : 
            if i >= s_len or j >= s_len : 
                return 0
            
            if s[i] == rev[j] : 
                return 1 + solve(i+1 , j+1)
            else : 
                return max(solve(i+1 , j) , solve(i , j+1))

        return solve(0 , 0)