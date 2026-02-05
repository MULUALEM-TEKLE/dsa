class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_range = max(nums)+1
        counter = [0] * max_range

        for num in nums : 
            counter[num] += 1 
        

        i = 0 
        for n in range(len(counter)) : 
            for _ in range(counter[n]) : 
                nums[i] = n
                i+= 1 
            