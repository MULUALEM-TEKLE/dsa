class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = {num:0 for num in nums}
        for num in nums : 
            count[num] += 1 

        def dfs():
            if len(perm) == len(nums) : 
                res.append(perm[:])

            for n in count : 
                if count[n] : 
                    perm.append(n)
                    count[n] -= 1

                    dfs()
                    count[n] += 1
                    perm.pop()
        
        dfs()
        return res