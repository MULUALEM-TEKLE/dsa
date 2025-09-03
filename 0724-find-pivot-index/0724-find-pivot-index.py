class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        rightsum = total
        for i,num in enumerate(nums) : 
            rightsum = total - leftsum - num

            if leftsum == rightsum : 
                return i 
            
            leftsum += num
        
        
        return -1