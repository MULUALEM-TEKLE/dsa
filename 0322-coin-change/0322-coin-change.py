class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo ={0:0}

        def find_ways(amt) : 
            if amt in memo : return memo[amt]
            minm = float("inf")
            for coin in coins : 
                diff = amt - coin 
                if diff < 0 : 
                    break
                minm = min(minm , 1+find_ways(diff))
            memo[amt] = minm
            return memo[amt]
                
        
        result = find_ways(amount)
        print(memo)
        if result < float("inf") : return result
        return -1