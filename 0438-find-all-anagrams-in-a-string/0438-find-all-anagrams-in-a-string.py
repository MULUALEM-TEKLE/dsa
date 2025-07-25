class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnt = Counter(p)
        p_len = len(p)
        res = []
        for i in range(len(s)-p_len+1) : 
            if Counter(s[i : i+p_len]) == p_cnt : res.append(i)
        return res