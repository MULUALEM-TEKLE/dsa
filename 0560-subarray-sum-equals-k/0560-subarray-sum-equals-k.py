class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = defaultdict(int)
        table[0] = 1  
        cur = 0
        res = 0 
        for num in nums : 
            cur += num 
            if cur - k in table : 
                res += table[cur-k]
            table[cur] = 1 
        
        return res