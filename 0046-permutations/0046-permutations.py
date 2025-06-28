class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums : 
            new_perm = []
            for perm in perms : 
                for i in range(len(perm) + 1) : 
                    pc = perm[:]
                    pc.insert(i , num)
                    new_perm.append(pc)
            perms = new_perm 
        return perms 