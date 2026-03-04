from functools import cache 
from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        square_options = []

        for i in range(1 , int(sqrt(n))+1) : 
            square_options.append(i**2)
        @cache
        def explore(remaining) : 
            if remaining == 0 : 
                return 0
            ways = float('inf') 
            for square in square_options : 
                if remaining-square < 0 : 
                    break 
                ways = min(ways , 1 +explore(remaining-square))
            
            return ways

        return explore(n)