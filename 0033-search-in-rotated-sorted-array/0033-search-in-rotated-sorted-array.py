class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums)-1
        pivot = 0

        while left < right : 
            mid = (left+right)//2

            if nums[mid] > nums[right] : 
                pivot = mid + 1
                right = mid - 1
            else : 
                left = mid + 1
        
        print(pivot)
        
        left , right = 0 , len(nums)-1
        while left <= right : 
            mid = (left+right)//2
            mid2 = (mid+pivot)%len(nums)
            if nums[mid2] > target : 
                right = mid - 1
            elif nums[mid2] < target : 
                left = mid + 1
            else : 
                return mid2
            
        return -1