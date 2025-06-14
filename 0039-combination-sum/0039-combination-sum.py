class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset= []
        def dfs(i , cur_sum) : 
            if cur_sum > target or i >= len(candidates) : 
                return 
            
            if cur_sum == target : 
                if subset not in res : res.append(subset[:])
                # return 
            
            subset.append(candidates[i])
            dfs(i , candidates[i] + cur_sum)
            subset.pop()
            # while i + 1 < len(candidates) and candidates[i]==candidates[i+1] : 
            #     i += 1 
            dfs(i+1 ,cur_sum)
        
        dfs(0 , 0)
        return res