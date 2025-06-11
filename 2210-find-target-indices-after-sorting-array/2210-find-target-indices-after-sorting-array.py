class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        table = {}
        res = []

        for index, num in enumerate(nums) : 
            if num in table : 
                table[num].append(index)
            else : 
                table[num] = [index]
    
        if target in table : 
            res.extend(table[target])
            return res
        else : 
            return []
            
        
        # or

        # return [ i for i, num in enumerate(sorted(nums))) if num == target]
                
        
    
        



    