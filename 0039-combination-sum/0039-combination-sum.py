class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res  = []

        comb = []

        def dfs(i , cur_sum) : 
            if cur_sum == target : 
                res.append(comb[:])
                return 

            if cur_sum > target or i >= len(candidates)  : 
                return 

            # if cur_sum + candidates[i] > target : 
            #     return 

            comb.append(candidates[i])
            dfs(i , cur_sum + candidates[i])
            comb.pop()
            dfs(i + 1 , cur_sum)

        dfs(0 , 0)
        return res 
