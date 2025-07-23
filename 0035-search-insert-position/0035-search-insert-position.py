class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums)-1
        pos = len(nums)

        while left <= right : 
            mid = (left+right)//2

            if nums[mid] > target : 
                right = mid-1
                pos = mid 
            elif nums[mid] < target : 
                left = mid+1
            else : 
                return mid
        return pos

