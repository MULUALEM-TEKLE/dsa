class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        subset = []
        def dfs(i , current_sum) : 
            if current_sum == target : 
                # if subset not in res :
                res.append(subset[:])
                return
                
            if i >= len(candidates) or current_sum > target : 
                return 

            
            subset.append(candidates[i])
            dfs(i+1 , current_sum + candidates[i] )
            subset.pop()
            unique_index = i + 1 
            while unique_index < len(candidates) and candidates[i] == candidates[unique_index] : 
                unique_index += 1 
            dfs(unique_index , current_sum )

        dfs(0 , 0)
        return res 
