class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def roll(i , cur_target) : 
            # if i <= 0 : return 0
            if i == 0 : 
                return 1 if cur_target == 0 else 0
    

            ways = 0 
            for face in range(1 , k+1) : 
                ways += roll(i-1 , cur_target - face)
            return ways 
        return roll(n , target) % ((10**9) + 7)