class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = ((10**9) + 7)
        @cache
        def roll(i , trgt) : 
            if i == n and trgt == 0 : 
                return 1

            if i >= n  : return 0

            ways = 0
            for face in range(1 , k+1) : 
                if trgt - face < 0 : break
                ways += roll(i+1 , trgt - face)
            return ways 
        
        return roll(0 , target) % MOD
