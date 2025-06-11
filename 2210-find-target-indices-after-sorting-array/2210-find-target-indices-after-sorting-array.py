class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # ans = []

        # for index , num in enumerate(sorted(nums)) : 
        #     if num == target : 
        #         ans.append(index)
        
        # return ans

        lt = eq = 0

        for num in nums : 
            if num < target : 
                lt += 1 
            elif num == target : 
                eq += 1 
        
        return list(range(lt , lt + eq))