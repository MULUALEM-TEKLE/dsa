class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[left] != 0 : 
                    left += 1 
                    continue
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        """
        Do not return anything, modify nums in-place instead.
        """
        