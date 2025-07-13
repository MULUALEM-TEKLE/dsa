class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = [1 , 2]
        for i in range(2 , n+1) :
            dp[0] , dp[1] = dp[1], dp[0] + dp[1]
        return (dp[1] * dp[1]) % ((10**9) + 7)