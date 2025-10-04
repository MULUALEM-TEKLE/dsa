class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        res = 0
        cur = 0

        for num in nums : 
            cur += num
            if cur - k in freq : 
                res += freq[cur-k]
            freq[cur] += 1 
        
        return res