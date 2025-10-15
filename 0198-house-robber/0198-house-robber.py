class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def explore(i) : 
            # base cases 
            if i == 1 : 
                return max(nums[0] , nums[1])
            if i == 0 : 
                return nums[0]

            return max(nums[i] + explore(i-2) , explore(i-1))
        
        return explore(len(nums)-1)