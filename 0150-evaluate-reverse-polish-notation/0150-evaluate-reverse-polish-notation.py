import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens : 
            if token == "+": 
                a, b, = stack.pop(), stack.pop()
                stack.append(b+a)
            elif token == "/": 
                a, b, = stack.pop(), stack.pop()
                temp = b/a
                if temp < 0 : 
                    stack.append( math.ceil(temp))
                else : 
                     stack.append(math.floor(temp))
            elif token == "*": 
                a, b, = stack.pop(), stack.pop()  
                stack.append(b*a)
            elif token == "-": 
                a, b, = stack.pop(), stack.pop()
                stack.append(b-a)
            else : 
                stack.append(int(token))


        return stack[0]