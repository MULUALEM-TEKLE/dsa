class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_table = Counter(p)
        N = len(p)
        left = 0
        window_table = Counter(s[0 : N])
        res = []
        while left < len(s)-N+1 : 
            window_table = Counter(s[left : left+N])
            if window_table == p_table : 
                res.append(left)
            # window_table = {}
            left += 1 
        return res 