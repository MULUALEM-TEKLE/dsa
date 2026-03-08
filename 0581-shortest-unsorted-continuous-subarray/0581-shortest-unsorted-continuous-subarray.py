class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        r = 0 
        cur_max = nums[0]

        for i in range(1 , n) : 
            if nums[i] < cur_max : 
                r = i
            else : 
                cur_max = nums[i]
        
        l = 0 
        cur_min = nums[-1]

        for i in range(n-2 , -1 ,-1) : 
            if nums[i] > cur_min : 
                l = i 
            else : 
                cur_min = nums[i] 
        
        return 0 if l >= r else r-l+1