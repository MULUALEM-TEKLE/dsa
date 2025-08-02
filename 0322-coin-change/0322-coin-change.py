class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def change(amt) : 
            if amt == 0 : return 0

            minm = float("inf")

            for coin in coins : 
                if amt - coin >= 0 : 
                    minm = min(minm , 1+change(amt-coin))

            return minm
        
        res = change(amount)
        if res == float('inf') : return -1
        return res