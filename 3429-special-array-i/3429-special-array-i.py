class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def parity(n) : 
            if n % 2 == 0 : 
                return "even"
            else : 
                return "odd"
        for i in range(1 , len(nums)) : 
            if parity(nums[i]) == parity(nums[i-1]) : 
                return False
        return True