class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        @cache
        def change(amt) : 
            if amt <= 0 : return 0
            minm = float('inf')
            for coin in coins : 
                diff = amt-coin
                if diff < 0 : break 
                minm = min(minm , 1+change(diff))
            return minm 
        
        res = change(amount)
        return res if res != float('inf') else -1