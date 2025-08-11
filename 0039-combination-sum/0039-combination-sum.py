class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(i , cur) : 
            if i >= len(candidates) or cur > target : 
                return

            if cur == target : 
                res.append(comb[:]) 
                return


            
            comb.append(candidates[i])
            backtrack(i , candidates[i]+cur)
            comb.pop()
            backtrack(i+1 , cur)
        
        backtrack(0 , 0)
        return res