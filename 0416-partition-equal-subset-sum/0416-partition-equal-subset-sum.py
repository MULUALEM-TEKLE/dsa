class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0 : return False
        target = total // 2

        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1 , -1) : 
            nextdp = set()
            for t in dp :
                if nums[i]+t == target :
                    return True
                nextdp.add(t)
                nextdp.add(nums[i]+t)
            dp = nextdp

        return target in dp


        # @cache
        # def explore(i , cur) : 
        #     if cur == target : 
        #         return True 
        #     if i == len(nums) : 
        #         return False
            
        #     return explore(i+1 , cur+nums[i]) or explore(i+1 , cur)
        
        # return explore(0 , 0)