import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        if x > 0 and x < 10 : return True

        reversed = 0
        check = x
    
        while x > 0:
            
            reversed += (x%10) 
            if x < 10 :  break
            reversed *= 10
            x = (x // 10)
        
        print

        

        return check == reversed


        