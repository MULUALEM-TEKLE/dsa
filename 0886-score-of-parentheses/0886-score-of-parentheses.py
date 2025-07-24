'''
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
-> s = "()()" score 2 we just add 1 and 1
(A) has score 2 * A, where A is a balanced parentheses string.
-> s = "(())" score 2 because the inner parentheses has a score of 1 and the outer multiplies it by 2
-> s = "((()))" score 4 just multiply the above by 2
approach : 
-> use stack
    -> [0] first element will always be an opening, so for opening parentheses we just store 0
    -> when we get a ')' we pop the top of the stack add 1 to the top of the stack
        -> this work only for basic cases, what if s = "((()))" our approach will give [3] which is wrong
        -> after poping the top if its 1 that means we have a nested parentheses so we have to go 
        with the 3rd rule, 
            -> after popping we have to either add 1 or 2 * the popped element
            -> the maximum of two, if we have just an opened parentheses at the top it will be 1, 
            if we just get a nested one it will be 2 
'''

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s : 
            if c == '(' : 
                stack.append(0)
            else : 
                top = stack.pop()
                stack[-1] += max(2*top , 1)
        return stack[-1]