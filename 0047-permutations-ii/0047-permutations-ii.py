class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = {}
        for num in nums : 
            count[num] = count.get(num , 0) + 1 

        def dfs():
            if len(perm) == len(nums) : 
                res.append(perm[:])
                return

            for n in count : 
                if count[n] : 
                    perm.append(n)
                    count[n] -= 1

                    dfs()
                    count[n] += 1
                    perm.pop()
        
        dfs()
        return res