class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1 , amount+1) : 
            # minm = float('inf')
            for coin in coins : 
                diff = i-coin
                if diff < 0 : 
                    break
                dp[i] = min(dp[i] , dp[i-coin]+1)
                # minm = min(minm , dp[diff]+1)
            # dp[i] = minm
        return dp[amount] if dp[amount] != float('inf') else -1