class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  
        maxp = float('-inf')

        for right in range(1 , len(prices)) : 
            curp = prices[right]-prices[left]
            if curp <= 0 : 
                left = right
            maxp = max(maxp , curp )
        
        return maxp if maxp > 0 else 0
            