class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        subset = []
        def dfs(i , cur_sum) : 
            if cur_sum == target : 
                res.append(subset[:])

            if i >= len(candidates) or cur_sum > target or cur_sum + candidates[i] > target : 
                return

            subset.append(candidates[i])
            dfs(i , cur_sum + candidates[i])
            subset.pop()
            dfs(i + 1 , cur_sum)
        
        dfs(0 , 0)
        return res
        