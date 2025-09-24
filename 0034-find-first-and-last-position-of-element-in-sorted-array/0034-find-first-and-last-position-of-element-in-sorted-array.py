class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bounds(index) : 
            left = right = index
            while left > 0 and nums[left] == nums[left-1]: 
                left -= 1 
            
            while right < len(nums)-1 and nums[right] == nums[right+1] : 
                    right += 1 
            
            return [left , right]
        

        low , high = 0 , len(nums)-1

        while low <= high : 
            mid = (low+high)//2
            if nums[mid] > target : 
                high = mid - 1 
            elif nums[mid] < target : 
                low = mid + 1 
            else : 
                return bounds(mid)
        
        return [-1 , -1]