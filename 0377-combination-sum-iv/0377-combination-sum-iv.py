class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        @cache
        def dfs(cur) : 
            # if cur < 0 : 
            #     return 0
            if cur == 0 : 
                return 1 
            res = 0 
            for num in nums : 
                if cur-num < 0 : 
                    break
                res += dfs(cur - num)
            
            return res
            # return sum(dfs(cur-num) for num in nums)
        
        return dfs(target)

