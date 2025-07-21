class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute(sub) : 
            if len(sub) == 0 : 
                return [[]]
            
            perms = permute(sub[1:])
            res = []
            for perm in perms : 
                for i in range(len(perm)+1): 
                    pc = perm[:]
                    pc.insert(i , sub[0])
                    if pc not in res : res.append(pc)
            return res 
        return permute(nums)