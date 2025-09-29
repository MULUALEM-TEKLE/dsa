class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb(i) : 
            if i < 2 : 
                return 1 
            if i == 2 : 
                return 2 
            return climb(i-1) + climb(i-2)
        
        return climb(n)