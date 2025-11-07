class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m , n = len(s) , len(p)
        pcounter = Counter(p)
        res = []

        for i in range(0 , m-n+1) : 
            if pcounter == Counter(s[i : i+n]) : 
                res.append(i)
        
        return res 
