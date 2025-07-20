class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1 : 
            return nums[0]
        
        prev , cur = nums[0] ,max(nums[0], nums[1])

        for i in range(2 , len(nums)) : 
            prev , cur = cur , max(nums[i]+prev , cur)
        
        return cur