class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # table = {}
        # for num in nums : 
        #     if num in table.keys() : 
        #         table[num] += 1
        #     else : 
        #         table[num] = 1

        # for key, value in table.items() : 
        #     if value == 1 : 
        #         return key

        res = 0 
        for num in nums :
            res = res ^ num

        return res
