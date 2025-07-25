class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1 : return 0
        @cache
        def do(count , paste) : 
            if count == n : return 0
            if count > n : return float('inf')
            paste = 1 + do(count+paste , paste)
            copy = 2 + do(count+count , count)

            return min(copy , paste)
        
        return 1 + do(1 , 1)