class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        res = []

        def backtrack(i , comb , cur) : 
            if cur == target : 
                res.append(comb[:])
                return 


            if i >= len(nums) or cur > target : 
                return 

            if cur+nums[i] > target : 
                return
            comb.append(nums[i])
            backtrack(i+1 , comb , cur+nums[i])
            comb.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1] : 
                i += 1
            backtrack(i+1 , comb , cur)

        backtrack(0 , [] , 0)

        return res 