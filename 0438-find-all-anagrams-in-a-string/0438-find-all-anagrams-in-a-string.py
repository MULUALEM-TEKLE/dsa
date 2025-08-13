class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lens = len(s)
        lenp = len(p)

        p_table = Counter(p)
        res = []

        for i in range(lens-lenp+1) : 
            if s[i] not in p : 
                continue
            if Counter(s[i:i+lenp]) == p_table : 
                res.append(i)
        
        return res