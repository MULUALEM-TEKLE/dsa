class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0
        cursum = 0

        for right in range(len(nums)) : 
            cursum += nums[right]
            while cursum >= target : 
                res = min(res , right-left+1)
                cursum -= nums[left]
                left += 1 
                
        return res if res != float('inf') else 0