class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_map = {}

        for num in nums : 
            count_map[num] = count_map.get(num , 0) + 1
        
        for _ , value in count_map.items() :
            if value >= 2 : 
                return True
            
        return False 