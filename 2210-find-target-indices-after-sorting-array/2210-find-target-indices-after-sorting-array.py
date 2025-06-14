class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()
        table = {}

        for index,num in enumerate(nums) : 
            if num in table : 
                table[num].append(index)
            else : 
                table[num] = [index]
        
        if target in nums : res.extend(table[target])

        return res
