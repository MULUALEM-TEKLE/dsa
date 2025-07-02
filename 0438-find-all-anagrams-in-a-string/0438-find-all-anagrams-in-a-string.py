class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_table = Counter(p)
        N = len(p)
        left = 0
        res = []
        window_table = {}
        while left < len(s)-N+1 : 
            if s[left] not in p : 
                left += 1 
                continue 
            window_table = Counter(s[left : left+N])
            if window_table == p_table : 
                res.append(left)
            # window_table = {}
            left += 1 
        return res 
