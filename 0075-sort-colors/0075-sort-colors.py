class Solution:
    def sortColors(self, nums: List[int]) -> None:
        max_range = max(nums) + 1
        counter = [0] * max_range

        for num in nums :
            counter[num] += 1
        print(counter)
        nums.clear()
        for i in range(len(counter)):
            nums.extend([i] * counter[i])
        
        print(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
        