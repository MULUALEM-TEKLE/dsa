class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i) : 
            if len(subset) == k : 
                res.append(subset[:])
                return
            
            if i < 1 : 
                return 
            
            subset.append(i)
            dfs(i - 1)
            subset.pop()
            dfs(i - 1)
        
        dfs(n)

        return res
