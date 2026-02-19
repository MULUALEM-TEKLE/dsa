class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        sub = []

        def dfs(i) : 
            if i == len(nums) : 
                res.append(sub[:])
                return

            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1] : 
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res 