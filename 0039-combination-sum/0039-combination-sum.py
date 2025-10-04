class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        res = []

        comb = []

        def dfs(i , cur) : 
            if i == len(nums) or cur > target : 
                return 
            
            if cur == target : 
                res.append(comb[:])
                return 

            comb.append(nums[i]) 
            dfs(i , cur + nums[i])
            comb.pop()
            dfs(i+1 , cur)
        
        dfs(0 , 0)

        return res 
