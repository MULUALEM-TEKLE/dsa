class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        cur = 0
        for i , num in enumerate(nums) : 
            if cur == total - cur - num : return i
            cur += num
        
        return -1