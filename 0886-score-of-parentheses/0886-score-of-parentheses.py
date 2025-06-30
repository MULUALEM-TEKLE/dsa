class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for p in s : 
            if p == "(" : 
                stack.append(0)
            else : 
                prev = stack.pop()
                stack[-1] += max(2*prev , 1)
            print(stack)

        return stack[0]