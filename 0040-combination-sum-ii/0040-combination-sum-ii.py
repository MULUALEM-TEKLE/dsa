class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        res = []

        def dfs(i , cur , comb ) : 
            if cur == target : 
                res.append(comb[:])
                return 

            if i == len(nums) or cur > target : 
                return 
            
            if cur+nums[i] > target : 
                return

            comb.append(nums[i])
            dfs(i+1 , cur+nums[i] , comb)
            comb.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1] : 
                i += 1 
            dfs(i+1 , cur , comb)

        dfs(0 , 0 , [])

        return res