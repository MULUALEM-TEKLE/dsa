class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort() 
        res = []
        comb = []
        def backtrack(i , cur_sum) : 
            # base case 
            if cur_sum > target : 
                return
            if i == len(nums) : 
                if cur_sum == target : 
                    res.append(comb[:])
                return
            # recursive case
            comb.append(nums[i])
            backtrack(i+1 , cur_sum + nums[i])
            comb.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1] : 
                i += 1 
            backtrack(i+1 , cur_sum)
        backtrack(0 , 0) 
        return res 