class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        comb = []
        def dfs(i , cur) : 
            if cur > target : return
            if cur == target : 
                res.append(comb[:])
                return
            if i >= len(candidates) : 
                return 
            if candidates[i] + cur > target : 
                return
            comb.append(candidates[i])
            dfs(i+1 , cur + candidates[i])
            comb.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]: 
                i+=1
            dfs(i+1 , cur)
        dfs(0,0)
        return res