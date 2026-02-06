class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = Counter(p)
        window = defaultdict(int)
        p_len = len(p)
        if p_len > len(s) : return []
        for i in range(p_len) : 
            window[s[i]] += 1 
        res = [0] if p_dict == window else []

        left = 0
        
        for right in range(p_len , len(s)) : 
            window[s[left]] -= 1 
            if window[s[left]] == 0 : del window[s[left]]
            window[s[right]] += 1 

            left += 1 

            if window == p_dict : 
                res.append(left)

        
        return res