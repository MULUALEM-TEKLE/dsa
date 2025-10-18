class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = (10**9)+7

        limit = 0 
        base = 1 
        while True : 
            term = base ** x 
            if term > n : 
                break 
            limit = base 
            base += 1 

        
        @cache
        def explore(cur , lim) : 
                
            if lim < 0 or cur < 0 : 
                return 0
                
            if cur == 0 : 
                return 1

            res = 0
            for i in range(lim , 0 , -1) :
                if cur - i**x < 0 : continue
                res += explore(cur - i**x , i-1)
            
            return res % MOD

        return explore(n , limit) 

