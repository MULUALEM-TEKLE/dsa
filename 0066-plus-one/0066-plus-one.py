class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) -1 , -1 , -1) : 
            res = digits[i] + 1
            if res >= 10 : 
                digits[i] = res%10
                carry = 1
            else : 
                digits[i] = res
                carry = 0
                break
    
            
        if carry : 
            return [1] + digits
        else : 
            return digits
