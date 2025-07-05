class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n , cache) : 
            if n <= 1 : 
                return 1
            if n in cache : 
                return cache[n]
            cache[n] = climb(n-1 , cache) + climb(n-2 , cache)
            return cache[n]
        return climb(n , {})