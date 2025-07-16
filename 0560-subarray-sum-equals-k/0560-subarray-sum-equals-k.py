class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0 : 1}
        count = 0 
        cs = 0
        
        for num in nums : 
            cs += num 
            x = cs - k 
            count += freq.get(x , 0)
            freq[cs] = freq.get(cs , 0) + 1 

        return count