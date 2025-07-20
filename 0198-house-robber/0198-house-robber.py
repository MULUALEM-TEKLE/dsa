class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def steal(n) : 
            if n < 0 : 
                return 0
            return max(nums[n] + steal(n-2) , steal(n-1))

        return steal(len(nums)-1)