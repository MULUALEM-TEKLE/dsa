class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(opened , closed, s) : 
            if opened == closed == n : 
                res.append(s)
            
            if opened < n : 
                backtrack(opened+1 , closed , s+"(")
            if closed < opened : 
                backtrack(opened , closed+1 , s+")")
        
        backtrack(0 , 0 , "")
        return res