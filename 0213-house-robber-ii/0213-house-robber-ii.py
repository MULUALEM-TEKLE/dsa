class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = tuple(nums)
        @cache
        def steal(sub , i) : 
            if i == 0 : 
                return sub[0] 
            if i == 1 : 
                return max(sub[0] , sub[1])
            
            return max(sub[i] + steal(sub , i-2) ,steal(sub , i-1))
        
        N = len(nums)

        if N == 1 : 
            return nums[0]
        if N == 2 : 
            return max(nums)
        
        print(nums[1:])
        print(nums[:-1])

        return max(steal(nums[1:] , N-2) , steal(nums[:-1] , N-2))        