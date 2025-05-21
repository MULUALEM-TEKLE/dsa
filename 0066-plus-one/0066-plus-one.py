class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in range(len(digits)) : 
            number += digits[i] * (10 ** (len(digits)-1 - i ))
        
        number += 1

        result = []

        while number > 0 : 
            digit = number % 10
            number = number // 10
            result.append(digit)
        
        result.reverse()
        print(result)

        return result 

      
            
