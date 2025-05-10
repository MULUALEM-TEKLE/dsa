class Solution:
    def sortColors(self, nums: List[int]) -> None:
        max_range = max(nums) + 1
        counter = [0] * max_range

        for num in nums :
            counter[num] += 1
        print(counter)
        # nums.clear()
        # for i in range(len(counter)):
        #     nums.extend([i] * counter[i])
        
        # print(nums)
        i = 0
        for n in range(len(counter)):
            for _ in range(counter[n]) : 
                nums[i] = n
                i +=1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        