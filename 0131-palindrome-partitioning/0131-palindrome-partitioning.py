class Solution:
    def partition(self, s: str) -> List[List[str]]:
      
        
        res = []
        
        def dfs(i , part) : 
            if i >= len(s) : 
                res.append(part[:])
            
            for j in range(i , len(s)) : 
                c = s[i : j + 1]
                if c == c[::-1] : 
                    part.append(s[i : j+1])
                    dfs(j+1 , part)
                    part.pop()
        dfs(0 , [])
        return res