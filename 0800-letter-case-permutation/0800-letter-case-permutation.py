class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def dfs(i , cur) : 
            if i == len(s) : 
                res.append(cur)
                return 
            if s[i].isalpha() : 
                cur += s[i].lower()
                dfs(i+1 , cur)
                cur = cur[:-1]
                cur += s[i].upper()
                dfs(i+1 , cur)
            elif s[i].isdigit() : 
                cur += s[i]
                dfs(i+1 , cur)
                cur = cur[:-1]
        dfs(0 , "")
        return res