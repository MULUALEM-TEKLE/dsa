class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0 : 1}
        cs = 0
        res = 0

        for num in nums : 
            cs += num
            x = cs - k
            if x in freq : 
                res += freq[x]
            freq[cs] = freq.get(cs , 0) + 1 
        
        return res