class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_range = max(nums) + 2 
        bucket = [0] * max_range

        for num in nums : 
            bucket[num + 1 ] += 1 
        
        for i in range(1 , max_range) : 
            bucket[i] += bucket[i-1]
        
        return [bucket[num] for num in nums]

        