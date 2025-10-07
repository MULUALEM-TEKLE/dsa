class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i , cur) : 
            if i == len(coins) : 
                return 0

            if cur > amount : 
                return 0
            
            if cur == amount : 
                return 1 

            return dfs(i , cur + coins[i]) + dfs(i+1 , cur)

        return dfs(0 , 0)