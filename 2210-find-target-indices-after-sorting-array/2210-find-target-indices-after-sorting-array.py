class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []

        for index , num in enumerate(sorted(nums)) : 
            if num == target : 
                ans.append(index)
        
        return ans