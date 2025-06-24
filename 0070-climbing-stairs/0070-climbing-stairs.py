class Solution:
    def climbStairs(self, n: int ) -> int:
        def memo(n , cache) : 
            if n <= 2 :
                return n 

            if n in cache : 
                return cache[n]

            cache[n] = memo(n-1 , cache) + memo(n-2 , cache)
            return cache[n]
        return memo(n , {})
        