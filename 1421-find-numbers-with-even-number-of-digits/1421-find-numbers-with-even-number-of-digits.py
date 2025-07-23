class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def isEvenDigit(num) : 
            digit_count = 0
            while num > 0 : 
                num //= 10
                digit_count += 1 
            return 1 if digit_count % 2 == 0 else 0
        res = 0 
        for num in nums : 
            res += isEvenDigit(num)
        return res