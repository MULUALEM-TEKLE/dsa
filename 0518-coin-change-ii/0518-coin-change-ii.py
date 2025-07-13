class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def ways(i,amt) : 
            if i == len(coins) : 
                return 1 if amt == 0 else 0
            take = 0
            if amt >= coins[i] : 
                take = ways(i , amt-coins[i])
            leave = ways(i+1 , amt)
            return take + leave 
        return ways(0 , amount)
            