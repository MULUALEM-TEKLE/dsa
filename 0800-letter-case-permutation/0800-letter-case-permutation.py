class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtrack(i , cur) : 
            if i == len(s) : 
                res.append(cur)
                return 
            
            if s[i].isalpha() : 
                backtrack(i+1 , cur+s[i].upper())
                backtrack(i+1 , cur+s[i].lower())
            else : 
                backtrack(i+1 , cur+s[i])
        
        backtrack(0 , "")

        return res

            