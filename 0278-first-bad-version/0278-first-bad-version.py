# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low , high = 0 , n 
        res = n
        while low <= high : 
            mid = (low + high) // 2

            if not isBadVersion(mid) : 
                low = mid + 1 
            else : 
                res = mid
                high = mid -1
        return res