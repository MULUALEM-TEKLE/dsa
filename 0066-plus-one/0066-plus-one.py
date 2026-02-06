class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        for i in range(len(digits)-1 , -1 , -1) : 
            res = digits[i] + 1
            if res < 10 : 
                digits[i] = res 
                return digits
            else : 
                digits[i] = 0

        return [1] + digits