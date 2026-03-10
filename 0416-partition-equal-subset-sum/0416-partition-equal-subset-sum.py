class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0 : return False
        target = total // 2

        @cache
        def explore(i , cur) : 
            if cur > target : 
                return False
            # if cur == target : 
            #     return True 
            if i == len(nums) : 
                return True if cur == target else False
            
            return explore(i+1 , cur+nums[i]) or explore(i+1 , cur)
        
        return explore(0 , 0)