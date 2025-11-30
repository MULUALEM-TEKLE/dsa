# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        ma = mountainArr
        n = ma.length() -1  
        def find_center() : 
            left , right = 0 , n
            center = -1 
            while left <= right : 
                mid = (left+right)//2

                if ma.get(mid) > ma.get(mid+1) : 
                    center = mid 
                    right = mid - 1 
                else : 
                    left = mid + 1 
            return center
        center = find_center()

        print(center)
        
        def search_left(start, end) : 
            while start <= end : 
                mid = (start + end ) // 2 
                if ma.get(mid) == target : 
                    return mid 
                elif ma.get(mid) > target : 
                    end = mid - 1
                else : 
                    start = mid + 1 
            return -1
        
        def search_right(start, end) : 
            while start <= end : 
                mid = (start + end ) // 2 
                if ma.get(mid) == target : 
                    return mid 
                elif ma.get(mid) > target : 
                    start = mid + 1 
                else : 
                    end = mid - 1
            return -1

        ls = search_left(0 , center)
        rs = search_right(center+1 , n)
        print(ls)
        print(rs)

        if ls == -1 or rs == -1: return max(rs , ls)
        return min(ls , rs)

              