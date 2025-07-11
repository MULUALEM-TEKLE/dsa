class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums :
            new_perms = []
            for perm in perms : 
                for i in range(len(perm)+1) : 
                    pc = perm[:]
                    pc.insert(i , num)
                    if pc not in new_perms : new_perms.append(pc)
            perms = new_perms

        return perms