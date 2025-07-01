class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        comb = []
        def dfs(i , cur) : 
            if cur > target : 
                return
            if cur == target : 
                res.append(comb[:])
                return 
            if i >= len(candidates) : 
                return
            if candidates[i] + cur > target : 
                return 
            comb.append(candidates[i])
            dfs(i , candidates[i]+cur)
            comb.pop()
            dfs(i+1 , cur)
        dfs(0 , 0)
        return res 