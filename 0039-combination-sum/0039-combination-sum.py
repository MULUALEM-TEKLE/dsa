class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []


        def dfs(i, comb , cur) : 
            if i == len(nums) or cur < 0 : 
                return 
            
            if cur == 0 : 
                res.append(comb[:])
                return
            
            if cur-nums[i] < 0 : 
                return
            
            comb.append(nums[i])
            dfs(i , comb , cur-nums[i])
            comb.pop()
            dfs(i+1 , comb , cur)
            

        
        dfs(0 , [] , target)

        return res 

            