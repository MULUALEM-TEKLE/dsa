class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        comb = []

        def backtrack(i , cur) : 
          
            if len(comb) == k and cur == n : 
                res.append(comb[:])
                return 
            
            if i < 1 or len(comb) == n: 
                return 
                
            comb.append(i)
            backtrack(i-1 , cur + i)
            comb.pop()
            backtrack(i-1 , cur)

        backtrack(9 , 0)

        return res