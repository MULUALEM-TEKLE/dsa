class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        table = defaultdict(int)

        for num in nums : 
            table[num] += 1 
        
        for key,val in table.items() : 
            if val > 1 : return key