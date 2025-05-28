class Solution:
    def mySqrt(self, x: int) -> int:

        low , high = 0 , x
        res = 0
        while low <= high : 
            mid = (low + high) // 2 
            if mid ** 2 > x : 
                high = mid - 1
            elif mid ** 2 < x : 
                res = mid
                low = mid + 1 
            else : 
                return mid 
            
        return res
        