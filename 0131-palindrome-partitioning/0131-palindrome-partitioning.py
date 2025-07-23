class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def backtrack(i) : 
            if i == len(s) : 
                res.append(part[:])
            
            for j in range(i , len(s)): 
                subs = s[i : j+1]
                if subs == subs[::-1] : 
                    part.append(subs)
                    backtrack(j+1)
                    part.pop()
        backtrack(0)
        return res