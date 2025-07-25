class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        res = []

        comb = []

        def backtrack(i , cs) : 
            if i == len(nums) and cs == target : 
                res.append(comb[:])
                return
            
            if cs > target or i >= len(nums) : 
                return 
            
            comb.append(nums[i])
            backtrack(i , cs+nums[i])
            comb.pop()
            backtrack(i+1 , cs)
        
        backtrack(0 , 0)
        return res