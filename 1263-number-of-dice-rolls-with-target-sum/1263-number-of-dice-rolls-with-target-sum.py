class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        def roll(i , cur) : 
            if (i,cur) in memo : return memo[(i , cur)]
            if i == n : return 1 if cur == 0 else 0

            ways = 0 

            for face in range(1 , k+1) : 
                diff = cur - face 
                if diff < 0 : break
                ways += roll(i+1 , diff)
            memo[(i , cur)] =  ways 
            return memo[(i , cur)]
        
        return roll(0 , target) % ((10**9)+7)