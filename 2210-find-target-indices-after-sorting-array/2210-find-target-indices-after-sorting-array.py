class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     j=i
        #     while j>0 and nums[j] < nums[j-1]:
        #         nums[j], nums[j-1] = nums[j-1], nums[j]
        #         j-=1
        
        return [ i for i, num in enumerate(sorted(nums)) if num == target]
                
        
    
        



    