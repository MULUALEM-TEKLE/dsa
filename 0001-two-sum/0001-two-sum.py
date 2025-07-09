class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = defaultdict(int)
        for idx,num in enumerate(nums) :
            rest = nums[idx+1:] 
            if target-num in rest : 
                return [idx , rest.index(target-num)+idx+1]
             