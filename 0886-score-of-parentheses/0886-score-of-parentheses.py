class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for c in s : 
            if c == "(" : 
                stack.append(0)
            else : 
                top = stack.pop()
                stack[-1] += max(top*2 , 1)
        return stack[0]