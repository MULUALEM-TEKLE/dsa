class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in coins : return 1 
        coins.sort()
        # coins = set(coins)
        memo = {}
        def find_ways( c) : 
            if c == 0 : 
                return 0 

            if c in memo : 
                return memo[c]

            minm = float('inf')
            for coin in coins : 
                diff = c - coin 
                if diff < 0 : break 
                minm = min(minm , 1+find_ways(diff))
            memo[c] = minm
            return memo[c]

        res = find_ways(amount)
        return res if res != float('inf') else -1