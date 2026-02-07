class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        res = []
        comb = []

        def dfs(i , target) : 
            if target == 0 : 
                res.append(comb[:])
                return
            if i >= len(nums) or target < 0 : 
                return  

            comb.append(nums[i])
            dfs(i , target-nums[i])
            comb.pop()
            dfs(i+1 , target)
        
        dfs(0 , target)
        return res 
            