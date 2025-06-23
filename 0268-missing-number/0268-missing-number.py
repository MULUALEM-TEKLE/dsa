class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n_xor = 0

        for i in range(len(nums)+1) : 
            n_xor = i ^ n_xor

        nums_xor = n_xor
        for num in nums : 
            nums_xor ^= num
        
        return nums_xor