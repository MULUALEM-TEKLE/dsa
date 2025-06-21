class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1 , -1 ,-1) : 
            cur_sum = digits[i] + 1 
            if cur_sum > 9 : 
                digits[i] = 0
            else : 
                digits[i] = cur_sum
                return digits 
        return [1] + digits