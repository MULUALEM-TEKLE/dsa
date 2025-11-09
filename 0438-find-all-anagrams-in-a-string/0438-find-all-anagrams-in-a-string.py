class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m , n = len(s) , len(p)
        pcounter = Counter(p)
        scounter = Counter(s[0 : n])
        res = [0] if pcounter == scounter else []
        left = 0

        for right in range(1 , m-n+1) : 
            scounter[s[left]] -= 1
            scounter[s[right+n-1]] += 1  
            if scounter[s[left]] == 0 : 
                del scounter[s[left]]
            left += 1

            if scounter == pcounter : 
                res.append(right) 
        
        return res 
