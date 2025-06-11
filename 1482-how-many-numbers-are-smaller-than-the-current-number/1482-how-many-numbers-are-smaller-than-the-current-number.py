class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        left = 0
        while left < len(nums) : 
            for i in range(len(nums)) : 
                if nums[i] < nums[left] : 
                    res[left] += 1
            left += 1 
            
        return res
            