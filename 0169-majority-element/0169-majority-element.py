class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        majority = len(nums)/2

        left = 0 
        length = 0
        for right in range(len(nums)) : 
            if nums[right] == nums[left] : 
                length += 1 
                if length >= majority : return nums[left]
                continue 
            left = right
            # length = 0
