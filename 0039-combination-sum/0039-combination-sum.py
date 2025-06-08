class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i , current_sum) : 
            if i >= len(candidates) or current_sum > target : 
                return 
            
            if current_sum == target : 
                res.append(subset[:])
                return
            
            subset.append(candidates[i])
            dfs(i , current_sum + candidates[i])
            subset.pop()
            dfs(i+1 , current_sum)
        
        dfs(0 , 0)
        return res