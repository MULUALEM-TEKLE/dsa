class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(cur) : 
            if cur < 0 : 
                return 0
            if cur == 0 : 
                return 1 
            res = 0 
            return sum(dfs(cur-num) for num in nums)
        
        return dfs(target)

