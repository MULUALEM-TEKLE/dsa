class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = [0]

        sub = []
        def dfs(i) : 
            if i >= len(nums) : 
                if sub == [] : return 
                xor_res = 0
                for num in sub : 
                    xor_res ^= num
                res[0] += xor_res
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            dfs(i+1)
        dfs(0)
        return res[0]