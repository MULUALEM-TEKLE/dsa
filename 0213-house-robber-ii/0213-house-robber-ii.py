class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = tuple(nums)
        @cache
        def steal(nums , i) : 
            if i == 0 : 
                return nums[0] 
            if i == 1 : 
                return max(nums[0] , nums[1])
            
            return max(nums[i] + steal(nums , i-2) ,steal(nums , i-1))
        
        N = len(nums)

        if N == 1 : 
            return nums[0]
        if N == 2 : 
            return max(nums)
        
        tmp = nums 
        nums = tmp[1:]
        loot_without_first_house = steal(nums , N-2)
        nums = tmp[:-1]
        loot_without_last_house = steal(nums , N-2)

        return max(loot_without_first_house , loot_without_last_house )        