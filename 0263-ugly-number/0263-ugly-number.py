class Solution:
    def isUgly(self, n: int) -> bool:
        for p in 2 , 3 , 5 : 
            while n and n % p == 0 : 
                n /= p 
        return n == 1 