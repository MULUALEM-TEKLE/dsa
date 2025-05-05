import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens : 
            if token == "+": 
                a, b, = stack.pop(), stack.pop()
                print(f"adding {a} and {b}")
                stack.append(b+a)
            elif token == "/": 
                a, b, = stack.pop(), stack.pop()
                print(f"dividing {b} by {a}")
                temp = b/a
                if temp < 0 : 
                    print('==== found -ve number ====')
                    stack.append( math.ceil(temp))
                else : 
                     stack.append(math.floor(temp))
                   
            elif token == "*": 
                a, b, = stack.pop(), stack.pop()
                print(f"mult {a} and {b}")
                stack.append(b*a)
            elif token == "-": 
                a, b, = stack.pop(), stack.pop()
                print(f"subtracting {a} from {b}")
                stack.append(b-a)
            else : 
                stack.append(int(token))


        return stack[0]