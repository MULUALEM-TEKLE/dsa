class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def steal(i) : 
            if i == 0 : 
                return nums[0] 
            if i == 1 : 
                return max(nums[:2])
            
            return max(nums[i] + steal(i-2) ,steal(i-1))
        
        return steal(len(nums)-1)