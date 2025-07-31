class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # n = len(text1)
        # m = len(text2)

        # dp = [[0]*(m+1) for _ in range(n+1)]

        # for i in range(1 , n+1) : 
        #     for j in range(1 , m+1) : 
        #         if text1[i-1] == text2[j-1] : 
        #             dp[i][j] = dp[i-1][j-1] + 1 
        #         else : 
        #             dp[i][j] = max( dp[i][j-1], dp[i-1][j])
        
        # return dp[n][m]

        n = len(text1)
        m = len(text2)
        @cache
        def longest(i , j) : 
            if i == n or j == m : return 0

            if text1[i] == text2[j] : 
                return 1 + longest(i+1 , j+1)
            else : 
                return max(longest(i+1 , j) , longest(i , j+1))
        
        return longest(0 , 0)