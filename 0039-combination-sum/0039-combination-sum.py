class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        res = []

        comb = []

        def backtrack(i , cs) : 
            if cs > target or i >= len(nums) : 
                return 

            if cs == target : 
                res.append(comb[:])
                return
            
            if nums[i] + cs > target : return
            comb.append(nums[i])
            backtrack(i , cs+nums[i])
            comb.pop()
            backtrack(i+1 , cs)
        
        backtrack(0 , 0)
        return res