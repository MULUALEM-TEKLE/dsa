class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def jump(i) : 
            if i == n-1 : 
                return True 
            can = False
            for j in range(nums[i] , 0 , -1) : 
                if i+j > n-1 :
                    continue 
                if i+j == n-1 : 
                    return True 
                can = can or jump(i+j)

            return can
        
        return jump(0)