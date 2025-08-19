class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = (10**9)+7
        memo = {}
        def roll(i , cur) : 
            if (i , cur) in memo : return memo[(i , cur)]
            if i == n : 
                return 1 if cur == target else 0
            
            ways = 0 

            for face in range(1 , k+1) : 
                if cur + face > target : break
                ways += roll(i+1 , cur + face)
            
            memo[(i , cur)] = ways

            return ways % MOD

        return roll(0 , 0) 