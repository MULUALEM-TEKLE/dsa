class Solution:
    def fib(self, n: int) -> int:
        if n == 0 : 
            return 0
        if n == 1 : 
            return 1
        dp = [0 , 1]

        for i in range(1 , n) : 
            dp[0] , dp[1] = dp[1] , dp[0]+dp[1]

        return dp[1]
        





        