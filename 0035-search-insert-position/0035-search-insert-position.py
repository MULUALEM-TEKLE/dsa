class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low , high = 0 , len(nums) - 1
        pos = len(nums)

        while low <= high : 
            mid = low + (high - low) // 2 

            if nums[mid] < target : 
                low = mid + 1
            else :
                pos = mid 
                high = mid - 1
          
        return pos        