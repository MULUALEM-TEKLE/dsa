class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        smallest = nums[0]
        for num in nums:
            if abs(num) < abs(smallest) :
                smallest = num

        if abs(smallest) in nums : 
            return abs(smallest)
        else:
            return smallest
        
        
       
        