class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = Counter(p)
        window = defaultdict(int)
        p_len = len(p)
        if p_len > len(s) : return []
        for i in range(p_len) : 
            window[s[i]] += 1 
        res = [0] if p_dict == window else []

        
        for i in range(1 , len(s)-p_len+1) : 
            window[s[i-1]] -= 1 
            if window[s[i-1]] == 0 : del window[s[i-1]]
            window[s[i+p_len-1]] += 1 

            if window == p_dict : 
                res.append(i)
        
        return res