class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 : 
            return 0
        @cache
        def do(i) : 
            if i == n-1 : 
                return 0 
            
            minm = float('inf')
            for j in range(nums[i] , 0 , -1) : 
                if i + j > n-1 : 
                    continue
                minm = min(minm , 1 + do(i+j))
            return minm
        
        return do(0)

        

