class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        subset = []

        def dfs(i) :
            if i >= len(s) : 
                tmp = "".join(subset)
                res.append(tmp)
                return

            if s[i].isalpha() : 
                subset.append(s[i].upper())
                dfs(i+1)
                subset.pop()
                subset.append(s[i].lower())
                dfs(i+1)
                subset.pop()
            else : 
                subset.append(s[i])
                dfs(i+1)
                subset.pop()
            
        
        dfs(0)
        return res