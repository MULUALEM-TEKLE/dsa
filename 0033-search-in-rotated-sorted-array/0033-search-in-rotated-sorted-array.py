class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums)-1

        while left < right : 
            mid = (left+right)//2

            if nums[mid] > nums[right] : 
                left = mid + 1
            else : 
                right = mid
        pivot = left

        left , right = 0 , len(nums)-1

        while left <= right : 
            mid = (left+right) // 2
            mid2 = (mid + pivot)%len(nums)

            if nums[mid2] == target : 
                return mid2
            elif nums[mid2] > target : 
                right = mid - 1
            else : 
                left = mid + 1 
        return -1   