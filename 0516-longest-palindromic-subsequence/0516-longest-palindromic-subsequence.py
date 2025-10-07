class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        r = s[::-1]

        n = len(s)

        memo = {}
        def solve(i , j) : 
            if (i , j) in memo : return memo[(i,j)]
            if i == n or j == n : 
                return 0 
            
            if s[i] == r[j] : 
                memo[(i,j)] = 1 + solve(i+1, j+1)
                return memo[(i,j)] 
            else : 
                memo[(i,j)] = max(solve(i , j+1) , solve(i+1 , j))
                return memo[(i,j)]
        
        return solve(0 , 0)