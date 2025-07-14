class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lt = eq = 0
        for num in nums : 
            if num < target : 
                lt += 1 
            if num == target : 
                eq += 1 
        return [*range(lt , lt+eq)]