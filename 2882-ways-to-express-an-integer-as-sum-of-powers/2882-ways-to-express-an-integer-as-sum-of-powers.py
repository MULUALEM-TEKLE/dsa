# class Solution:
#     def numberOfWays(self, n: int, x: int) -> int:
#         MOD = (10**9)+7

#         limit = math.floor(pow(n , 1/x))
        
#         @cache
#         def explore(cur , lim) : 
#             if cur == 0 : 
#                 return 1

#             if lim <= 0 : 
#                 return 0
#             if cur < 0 : 
#                 return 0
                

#             res = 0
#             for i in range(lim , 0 , -1) :
#                 if cur - i**x < 0 : continue
#                 res += explore(cur - i**x , i-1)
            
#             return res % MOD

#         return explore(n , limit) 

import math
from typing import List
from functools import lru_cache # Assuming @cache is lru_cache

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = (10**9)+7

        # --- FIX: Use robust integer method to calculate limit ---
        limit = 0
        base = 1
        while True:
            term = base ** x
    
            if term > n:
                break
            limit = base
            base += 1
        # --- End Fix ---
        
        # Use a more explicit @lru_cache if @cache is not a recognized alias
        @lru_cache(None)
        def explore(cur: int, lim: int) -> int:
            """
            Calculates the number of ways to achieve the sum 'cur' using 
            unique bases up to 'lim'.
            """
            
            if cur == 0: 
                return 1 # Found a valid combination
            if cur < 0 or lim <= 0:
                return 0 # Invalid state or no more bases to use

            res = 0
            
            # Iterate through possible unique bases 'i' from 'lim' down to 1
            for i in range(lim , 0 , -1):
                # Calculate i^x once per loop iteration
                term = i**x
                
                # Pruning: If the current term is too large, stop the loop 
                # (since 'i' is decreasing, all subsequent terms will also be too large).
                if cur - term < 0:
                    continue
                
                # Recursive Step:
                # If we include i^x, the remaining sum must be achieved using 
                # unique bases strictly smaller than i (i-1).
                res = (res + explore(cur - term, i - 1)) % MOD
                
            return res 

        return explore(n , limit)
