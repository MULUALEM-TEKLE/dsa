class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        pa = []
        def backtrack(op , cl ) : 
            if op == cl == n : 
                res.append("".join(pa))
                return 
            
            if op < n : 
                pa.append("(")
                backtrack(op+1 , cl)
                pa.pop()
            if cl < op : 
                pa.append(")")
                backtrack(op , cl+1)
                pa.pop()
        backtrack(0 , 0)
        return res
