class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 0
        for i in range(len(nums)) : 
            for j in range(i+1 , len(nums)) : 
                if nums[j] > nums[i] : 
                    dp[i] += 1 
            res = max(res , max(dp))
        return res
        '''
        @cache
        def explore(i) : 
            # if i == len(nums) : 
            #     return 0
            LIS = 1 
            for j in range(len(nums)-1 , i , -1) : 
                if nums[j] > nums[i] : 
                    LIS = max(LIS , 1+explore(j))
            return LIS
        
        res = 0

        for i in range(len(nums)) : 
            res = max(res , explore(i))
        
        return res
        '''