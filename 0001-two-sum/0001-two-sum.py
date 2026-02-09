class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cont = defaultdict(list)
        for index, num in enumerate(nums) : 
            cont[num].append(index)
        
        for index, num in enumerate(nums) : 
            if target - num in nums : 
                if num == target - num and len(cont[num]) > 1  : 
                    return cont[num]
                if index != cont[target-num][0] : 
                    return [index , *cont[target-num]]
            
        