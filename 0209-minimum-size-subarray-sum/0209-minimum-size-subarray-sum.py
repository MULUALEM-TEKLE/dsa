class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        right = 0 
        res = float('inf')
        while left <= right and right < len(nums) :
            if sum(nums[left : right+1]) < target : 
                right += 1
            else : 
                res = min(res , right-left+1)
                left += 1 
                right = left
        return res if res != float('inf') else 0
