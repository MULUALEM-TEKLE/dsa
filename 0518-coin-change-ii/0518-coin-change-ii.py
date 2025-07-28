class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def solve(i , amt) : 
            if amt == 0 : 
                return 1
            if i == len(coins) : return 0
            take = 0 
            if amt - coins[i] >= 0 : 
                take = solve(i , amt-coins[i])
            leave = solve(i+1 , amt)

            return take + leave
        
        return solve(0 , amount)