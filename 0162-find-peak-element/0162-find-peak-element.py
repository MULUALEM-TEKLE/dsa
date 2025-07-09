class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 : return 0
        def peak(idx) : 
            if idx == 0 :     
                return nums[idx] > nums[idx+1]
            elif idx == len(nums)-1 : 
                return nums[idx] > nums[idx-1]
            else : 
                return nums[idx] > nums[idx+1] and nums[idx] > nums[idx-1]

        for idx in range(len(nums)) : 
            if peak(idx) : 
                return idx