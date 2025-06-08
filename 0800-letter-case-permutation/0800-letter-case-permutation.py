class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        subset = []

        def dfs(i) :
            if i >= len(s) : 
                tmp = "".join(subset)
                if tmp not in res : res.append(tmp)
                return

            # if s[i].isnumeric() : 
            #     i += 1 
            
            subset.append(s[i].upper())
            dfs(i+1)
            subset.pop()
            subset.append(s[i].lower())
            dfs(i+1)
            subset.pop()
            
        
        dfs(0)
        return res