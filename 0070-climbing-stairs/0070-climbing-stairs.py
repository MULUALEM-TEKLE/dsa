class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0 : 1 , 1 : 1}
        def climb(n , cache) : 
            if n in cache : return cache[n]
            cache[n] = climb(n-1 , cache) + climb(n-2 , cache)
            return cache[n]
        return climb(n , cache)
        