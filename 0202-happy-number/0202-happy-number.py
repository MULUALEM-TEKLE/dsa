class Solution:
    def isHappy(self, n: int) -> bool:
        # square the digits and add them
        # repeat the process until I get to one 
        # register the numbers in a hashset, if they happen again I'll break out    
        seen = set()
        def helper(n) : 
            sq_sm = 0 
            while n > 0 : 
                sq_sm += (n % 10)**2
                n = n // 10
            if sq_sm in seen : return False
            seen.add(sq_sm)
            if sq_sm == 1 : return True 
            return helper(sq_sm)
        return helper(n)