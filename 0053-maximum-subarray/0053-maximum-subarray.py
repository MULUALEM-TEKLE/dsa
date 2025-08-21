class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxsum = nums[0]

        for num in nums : 
            if cur < 0 : 
                cur = 0 
            cur += num 
            maxsum = max(maxsum , cur)

        return maxsum