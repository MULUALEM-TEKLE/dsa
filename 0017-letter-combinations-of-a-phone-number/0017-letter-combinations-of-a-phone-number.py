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

        def explore(i , ch) : 
            if i == len(digits) : 
                res.append(ch)
                return
            for c in table[digits[i]] : 
                explore(i+1 , ch + c )
        
        explore(0 , "")

        return res 
            