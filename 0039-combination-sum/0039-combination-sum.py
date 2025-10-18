class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []


        def dfs(comb , cur) : 
            if cur == 0 : 
                comb = sorted(comb)
                if comb not in res : 
                    res.append(comb[:])
                return
            
            for num in nums : 
                if cur - num < 0 : break
                comb.append(num)
                dfs(comb , cur-num)
                comb.pop()
        
        dfs([] , target)

        return res 

            