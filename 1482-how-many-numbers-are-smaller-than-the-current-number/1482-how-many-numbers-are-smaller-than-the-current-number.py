class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = {}

        for index , num in enumerate(sorted(nums)) : 
            if num not in counter : 
                counter[num] = index
        
        return [counter[num] for num in nums]
        
