class Solution:
    def findMin(self, nums: List[int]) -> int:
        low , high = 0 , len(nums)-1
        pivot = 0
        while low < high : 
            mid = (low + high)//2

            if nums[mid] > nums[high] : 
                low = mid + 1 
                pivot = mid + 1
            else : 
                high = mid
        
        return nums[pivot]
        

        
