class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(n) : 
            if len(subset) == k : 
                res.append(subset[:])
                return
            
            if n < 1 : 
                return 
            
            subset.append(n)
            dfs(n-1)
            subset.pop()
            dfs(n-1)
        
        dfs(n)
        return res