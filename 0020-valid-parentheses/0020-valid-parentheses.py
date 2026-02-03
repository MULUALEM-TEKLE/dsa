class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(', '}':'{', ']':'['
        }

        for c in s : 
            if c in ['(', '{',  '['] : 
                stack.append(c)
            else : 
                if not stack or stack[-1] != table[c] : 
                    return False 
                stack.pop()

        return stack == []
                