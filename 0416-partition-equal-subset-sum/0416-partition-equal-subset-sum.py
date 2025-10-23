class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0 : return False
        target = total // 2

        # dp = set()
        # dp.add(0)

        # for i in range(len(nums)-1, -1 , -1) : 
        #     nextdp = set()
        #     for t in dp :
        #         summ = nums[i]+t
        #         if summ == target :
        #             return True
        #         nextdp.add(t)
        #         if summ > target : continue
        #         nextdp.add(summ)
        #     dp = nextdp

        # return target in dp


        # @cache
        # def explore(i , cur) : 
        #     if cur > target : 
        #         return False
        #     if cur == target : 
        #         return True 
        #     if i == len(nums) : 
        #         return False
            
        #     return explore(i+1 , cur+nums[i]) or explore(i+1 , cur)
        
        # return explore(0 , 0)

        n = len(nums)
        dp = [[0]*(target+1) for _ in range(n+1)]

        for i in range(n+1) : 
            dp[i][0] = 1
        
        for r in range(1 , n+1) : 
            num = nums[r-1]
            for c in range(1 , target+1) : 
                leave = dp[r-1][c]

                take = 0
                if c >= num : 
                    take = dp[r-1][c-num]

                dp[r][c] = take or leave
            if dp[r][target] : return True 
        

        return bool(dp[n][target])