class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1] : 
            return len(nums)
        elif target < nums[0] : 
            return 0

        left, right = 0 , len(nums) - 1
        # mid = (left + right)//2
        while left <= right : 
            mid = (left + right)//2
            # if left == right : 
            #     if nums[mid] >= target : 
            #         return mid 
            #     return mid + 1

            if nums[mid] > target : 
                right = mid - 1
            elif nums[mid] < target : 
                left = mid + 1
            else : 
                return mid
        
        return left 
