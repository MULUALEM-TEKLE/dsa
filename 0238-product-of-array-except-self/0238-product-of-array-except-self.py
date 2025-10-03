class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        for i in range(1 , n) : 
            left[i] = left[i-1] * nums[i-1]
        
        print(left)

        right = [1]*n
        for i in range(n-2 , -1 , -1) : 
            right[i] = right[i+1] * nums[i+1]
        
        return [l*r for r,l in zip(right,left)]