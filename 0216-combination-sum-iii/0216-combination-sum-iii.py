class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        comb = []
        def dfs(m , cs) : 
            if len(comb) == k and cs == n : 
                res.append(comb[:])

            if cs > n or len(comb) == k or m < 1 :
                return 

            comb.append(m)
            dfs(m-1 , cs+m)
            comb.pop()
            dfs(m-1 , cs)
        
        dfs(9 , 0)
        return res