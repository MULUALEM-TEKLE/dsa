class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = {}

        for num in nums : 
            table[num] = table.get(num , 0) + 1
        
        for num in nums : 
            if table[num] > 1 : 
                return True

        return False
         

