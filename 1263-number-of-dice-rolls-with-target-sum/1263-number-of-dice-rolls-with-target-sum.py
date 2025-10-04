class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = (10**9) + 7

        @cache
        def roll(i , cur_sum) : 
            if i == n : 
                return 1 if cur_sum == 0 else 0

            ways = 0 

            for face in range(1 , k+1) : 
                diff = cur_sum - face 
                if diff < 0 : break
                ways += roll(i+1 , diff)
            
            return ways 
        
        return roll(0 , target) % MOD