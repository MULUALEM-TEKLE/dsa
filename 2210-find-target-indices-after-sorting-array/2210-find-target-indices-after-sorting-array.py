class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []

        for index, num in enumerate(sorted(nums)) : 
            if num == target : 
                res.append(index)
        

        return res