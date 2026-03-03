class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        comb = []
        def dfs(i , cur) : 
            if len(comb) == k and cur == n : 
                res.append(comb[:])
                return 
            
            if i < 1 or cur > n: 
                return 
            
            comb.append(i)
            dfs(i-1 , cur+i)
            comb.pop()
            dfs(i-1 , cur)
        
        dfs(9 , 0)
        return res 