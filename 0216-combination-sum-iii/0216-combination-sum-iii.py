class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i) : 
            if len(subset) >= k : 
                if sum(subset) == n : 
                    res.append(subset[:])
                    return
                else : 
                    return 

            if i < 1 : 
                return 

            subset.append(i)
            dfs(i-1)
            subset.pop()
            dfs(i-1)
        
        dfs(9)
        return res