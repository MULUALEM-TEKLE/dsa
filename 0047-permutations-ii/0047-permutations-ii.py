class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1 : 
            return [nums[:]]

        for i in range(len(nums)): 
            n = nums.pop(0)
            perms = self.permuteUnique(nums)
            for perm in perms : 
                perm.append(n)
            for perm in perms : 
                if perm not in res : 
                    res.append(perm)
            nums.append(n)
        return res

