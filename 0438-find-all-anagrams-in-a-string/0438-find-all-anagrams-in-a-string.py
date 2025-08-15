class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lens = len(s)
        lenp = len(p)

        if lenp > lens : 
            return []

        ptable = defaultdict(int)
        stable = defaultdict(int)

        for i in range(lenp) : 
            ptable[p[i]] += 1 
            stable[s[i]] += 1 
        
        res = [0] if ptable == stable else []
        left = 0
        
        for right in range(lenp , lens) : 
            
            stable[s[right]] += 1 
            stable[s[left]] -= 1 


            if stable[s[left]] == 0 : 
                stable.pop(s[left])

            left += 1
            
            if stable == ptable : 
                res.append(left)
                
        return res 