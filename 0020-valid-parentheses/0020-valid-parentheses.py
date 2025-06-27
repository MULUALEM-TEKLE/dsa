class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        lookup = {"}" : "{" , ")" : "(" , "]" : "["}
        for c in s : 
            if c in lookup :
                if not stack : return False
                if stack[-1] == lookup[c] : 
                    stack.pop()
                else : return False
            else : 
                stack.append(c)
        return stack == []

