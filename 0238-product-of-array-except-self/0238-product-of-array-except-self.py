class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_mult = 1 
        left_arr = [0] * n 
        for i in range(n) : 
            left_arr[i] = left_mult
            left_mult *= nums[i]

        right_mult = 1 
        right_arr = [0] * n 
        for i in range(n-1 , -1 , -1) : 
            right_arr[i] = right_mult
            right_mult *= nums[i]

        return [l*r for l,r in zip(left_arr , right_arr)]