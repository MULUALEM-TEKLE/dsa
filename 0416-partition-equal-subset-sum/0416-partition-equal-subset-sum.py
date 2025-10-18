class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0 : 
            return False 
        half = total // 2

        @cache
        def explore(i , cur) : 
            if cur == 0 : 
                return True 

            if i == len(nums) or cur < 0: 
                return False


            return explore(i+1 , cur-nums[i]) or explore(i+1 , cur)


        return explore(0 , half)
