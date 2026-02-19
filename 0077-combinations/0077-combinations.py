class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        comb = []

        def dfs(i) : 


            if len(comb) == k : 
                res.append(comb[:])
                return
                   
            if i < 1 :
                return

            comb.append(i)
            dfs(i-1)
            comb.pop()
            dfs(i-1)
        
        dfs(n)
        return res
