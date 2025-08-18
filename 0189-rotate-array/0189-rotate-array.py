class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()

        k = k%len(nums)

        left = 0
        pivot = k-1

        while left < pivot : 
            nums[left] , nums[pivot] = nums[pivot] , nums[left]
            left += 1 
            pivot -= 1 
        
        left = k
        right = len(nums) - 1 
        while left <= right :
            nums[right] , nums[left] = nums[left] , nums[right]
            right -= 1 
            left += 1 