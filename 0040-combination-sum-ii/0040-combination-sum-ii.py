class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        subset = []
        def dfs(i , target_num) : 
            if i >= len(candidates) : 
                return
            
            target_num -= candidates[i]
            if target_num < 0 : 
                target_num += candidates[i]
                return
                
            subset.append(candidates[i])



            # print(target_num)
            if target_num == 0 : 
                res.append(subset[:])

            dfs(i + 1 , target_num)
            subset.pop()
            target_num += candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1] : 
                i += 1 
            dfs(i+1 , target_num)
        
        dfs(0 , target)
        return res
