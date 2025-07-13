class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def ways(i , amt) : 
            if amt == 0 : return 1 
            if i == len(coins) or amt < 0 : return 0
            return ways(i , amt-coins[i]) + ways(i+1 , amt)
        return ways(0 , amount)