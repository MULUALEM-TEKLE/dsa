class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        res = []

        comb = []

        def dfs(i , cur_sum) : 
            # base cases 
            if i == len(nums) or cur_sum < 0 : 
                return 
            
            if cur_sum == 0 : 
                res.append(comb[:])
                return

            comb.append(nums[i])
            dfs(i , cur_sum - nums[i])
            comb.pop()
            dfs(i+1 , cur_sum)
        
        dfs(0 , target)

        return res

