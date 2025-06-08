class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        subset = []

        def dfs(i) :
            if i >= len(s) : 
                if "".join(subset) not in res : res.append("".join(subset))
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