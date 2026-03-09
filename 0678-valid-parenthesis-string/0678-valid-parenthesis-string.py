class Solution:
    def checkValidString(self, s: str) -> bool:
        opened , closing = 0 , 0

        for c in s : 
            if c == "(" : 
                opened , closing = opened +1 , closing + 1 
            elif c == ")" : 
                opened , closing = opened - 1 , closing - 1 
            else : 
                opened , closing = opened - 1 , closing + 1

            if closing < 0 : return False
            if opened < 0 : opened = 0 
        
        print(opened)

        return opened == 0 
