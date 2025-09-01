class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left , right = 0 , len(nums)-1
        res = [0] * len(nums)
        n = len(nums)-1
        while left <= right : 
            if abs(nums[left]) > abs(nums[right]) : 
                res[n] = nums[left]**2
                left += 1 
            else : 
                res[n] = nums[right]**2
                right -= 1 
            n -= 1 
        
        return res
            