class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache 
        def explore(i) : 
            LIS = 1
            for j in range(i+1 , len(nums)): 
                if nums[j] > nums[i] : 
                    LIS = max(LIS , 1 + explore(j))
            return LIS
        
        res = 0
        return max(explore(i) for i in range(len(nums)))