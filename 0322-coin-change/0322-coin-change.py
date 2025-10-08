class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort()
        @cache
        def find_ways(cur) : 
            if cur == 0 : 
                return 0
            
            if cur < 0 : 
                return float('inf')
           
            minm = float('inf')
            for coin in coins : 
                diff = cur - coin
                # if diff < 0 : 
                #     break
                minm = min(minm , 1+find_ways(diff))
            return minm 
        
        res = find_ways(amount)
        return res if res != float('inf') else -1