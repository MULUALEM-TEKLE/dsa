class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        comb = []
        def dfs(m) : 
            if len(comb) == k : 
                res.append(comb[:])
                return
                
            if (n - m + 1) < (k - len(comb)) : 
                return 
            
            comb.append(m)
            dfs(m+1)
            comb.pop()
            dfs(m+1)

        dfs(1)
        return res