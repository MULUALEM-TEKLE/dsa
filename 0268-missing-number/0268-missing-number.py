class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums : return 0
        n = len(nums) 

        for i in range(n) : 
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i] : 
                correct_index = nums[i]-1
                nums[i] , nums[correct_index] = nums[correct_index] , nums[i]
        
        for i in range(n) : 
            if nums[i] != i+1 : 
                return i+1
        
        return n+1
       