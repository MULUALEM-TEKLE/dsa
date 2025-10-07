class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        r = s[::-1]

        n = len(s)

        @cache
        def solve(i , j) : 
            if i == n or j == n : 
                return 0 
            
            if s[i] == r[j] : 
                return 1 + solve(i+1, j+1)
            else : 
                return max(solve(i , j+1) , solve(i+1 , j))
        
        return solve(0 , 0)