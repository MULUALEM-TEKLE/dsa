class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lens = len(s)
        lenp = len(p)

        if lenp > lens : return []

        p_table = defaultdict(int)
        s_table = defaultdict(int)

        for i in range(lenp) : 
            p_table[p[i]] += 1 
            s_table[s[i]] += 1
            
        res = [0] if p_table == s_table else []

        left = 0

        for right in range(lenp , lens) : 
            s_table[s[right]] += 1 
            s_table[s[left]] -= 1

            if s_table[s[left]] == 0 : 
                s_table.pop(s[left])

            left += 1 

            if s_table == p_table : 
                res.append(left)
        
        return res