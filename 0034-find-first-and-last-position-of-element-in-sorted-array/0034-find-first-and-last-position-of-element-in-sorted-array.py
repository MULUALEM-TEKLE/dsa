class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1 , -1]
        left , right = 0 , len(nums)-1

        def find_bounds(mid) : 
            left = mid 
            while left > 0 and nums[left-1] == target : 
                left -= 1 
            right = mid
            while right < len(nums) - 1 and nums[right+1] == target : 
                right += 1 
            return [left , right]

        while left <= right : 
            mid = (left+right)//2

            if nums[mid] > target : 
                right = mid - 1
            elif nums[mid] < target : 
                left = mid + 1 
            else : 
                return find_bounds(mid)
            
        return res