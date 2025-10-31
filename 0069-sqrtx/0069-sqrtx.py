class Solution:
    def mySqrt(self, x: int) -> int:
        # 8 -> 4 -> 2 -> 3
        low , high = 0 , x
        res = x

        while low <= high : 
            mid = (low+high)//2

            if mid * mid > x : 
                high = mid-1
            elif mid * mid < x : 
                res = mid
                low = mid + 1 
            else : 
                return mid

        return res   