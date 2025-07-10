class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        # perm = []
        def backtrack(i , perm) : 
            if i >= len(s) : 
                res.append(perm)
                return 
            
            if s[i].isalpha() : 
                backtrack(i+1 , perm+s[i].upper())
                backtrack(i+1 , perm+s[i].lower())
                pass
            else : 
                backtrack(i+1 , perm+s[i])
        backtrack(0 , "")
        return res