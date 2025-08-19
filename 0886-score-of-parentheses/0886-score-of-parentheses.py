class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = []
        cur = 0

        for c in s : 
            if c == "(" : 
                res.append(cur)
                cur = 0
            else : 
                top = res.pop()
                cur = top +  max(1 , cur*2)
                
        
        return cur