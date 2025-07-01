class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2" : "abc" , 
            "3" : "def" , 
            "4" : "ghi" , 
            "5" : "jkl" , 
            "6" : "mno" , 
            "7" : "pqrs" , 
            "8" : "tuv" , 
            "9" : "wxyz" , 
        }

        res = []
        def dfs(i , cur_str) :
            if i >= len(digits) : 
                res.append(cur_str)
                return 
            for c in table[digits[i]] : 
                dfs(i+1 , cur_str + c)
        if not digits == "" :
            dfs(0 , "")
        return res 


       