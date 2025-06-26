class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 : 
            return [[]]
        
        perms = self.permuteUnique(nums[1:])
        res = []
        for p in perms : 
            for i in range(len(p)+1) : 
                pc = p[:]
                pc.insert(i , nums[0])
                if pc not in res : res.append(pc)
        return res