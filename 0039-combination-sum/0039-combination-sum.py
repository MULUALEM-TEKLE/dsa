class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        subset= []
        def dfs(i , cur_sum) : 
            if cur_sum > target or i >= len(candidates) : 
                return 
            
            if cur_sum == target : 
                res.append(subset[:])
                return 

            if cur_sum + candidates[i] > target :
                return

            subset.append(candidates[i])
            dfs(i , candidates[i] + cur_sum)
            subset.pop()
            dfs(i+1 ,cur_sum)
        
        dfs(0 , 0)
        return res