class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        lookup = {"}" : "{" , ")" : "(" , "]" : "["}
        for c in s : 
            if c in lookup :
                if not stack or stack[-1] != lookup[c] : return False
                stack.pop()
            else : 
                stack.append(c)
        return stack == []

