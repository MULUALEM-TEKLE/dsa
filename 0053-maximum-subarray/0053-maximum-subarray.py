class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        max_sum = nums[0]

        for n in nums : 
            if cur < 0 : 
                cur = 0
            cur += n
            max_sum = max(max_sum , cur)
        return max_sum