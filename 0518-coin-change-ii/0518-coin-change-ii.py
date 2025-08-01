class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i , amt) : 
            if i >= len(coins) : 
                return 1 if amt == 0 else 0
            
            if amt < 0 : 
                return 0
            
            
            # take = 0
            # if amt-coins[i] >= 0 :
            take = dfs(i , amt-coins[i])
            leave = dfs(i+1 , amt)

            return take + leave 
        
        return dfs(0 , amount)