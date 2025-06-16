class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1 , -1 , -1) : 
            res = digits[i] + 1 
            if res >= 10 : 
                digits[i] = res % 10
                carry = res // 10 
            else : 
                digits[i] = res 
                return digits
        return [1] + digits
