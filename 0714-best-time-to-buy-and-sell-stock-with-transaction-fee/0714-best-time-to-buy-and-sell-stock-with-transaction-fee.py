class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def explore(i , holding) : 
            if i >= len(prices) : 
                return 0
            if holding : 
                return max(prices[i]-fee + explore(i+1 , False) , explore(i+1 , True))
            else : 
                return max(-prices[i]+explore(i+1 , True) , explore(i+1 , False))
        return explore(0 , False)