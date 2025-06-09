class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        subset = []
        def dfs(i , current_sum) : 
            if current_sum == target : 
                res.append(subset[:])
                return

            if i >= len(candidates) or current_sum > target : 
                return 

            
            subset.append(candidates[i])
            dfs(i+1 , current_sum + candidates[i] )
            subset.pop()
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1] : 
                i += 1 
            dfs(i + 1 , current_sum )

        dfs(0 , 0)
        return res 
