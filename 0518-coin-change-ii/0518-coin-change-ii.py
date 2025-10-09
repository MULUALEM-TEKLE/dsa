class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def explore(i , x) : 
            if i == len(coins) or x > amount : 
                return 0
            if x == amount : 
                return 1
            
            return explore(i, x+coins[i]) + explore (i+1 , x)

        return explore(0,0)