class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def explore(i) : 
            # if i == len(nums) : 
            #     return 0
            lis = 1 
            for j in range(len(nums)-1 , i , -1) : 
                if nums[j] > nums[i] : 
                    lis = max(lis , 1+explore(j))
            return lis
        
        res = 0

        for i in range(len(nums)) : 
            res = max(res , explore(i))
        
        return res