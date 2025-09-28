class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums : 
            new_perms = []
            for perm in perms : 
                for p in range(len(perm)+1) : 
                    pc = perm[:]
                    pc.insert(p , num)
                    new_perms.append(pc)
            perms = new_perms
        
        return perms 