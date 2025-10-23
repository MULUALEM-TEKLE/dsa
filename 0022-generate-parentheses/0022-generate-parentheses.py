class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.output = []

        def build(opened , closed , res) : 
            if opened == closed == n : 
                self.output.append(res)
                return 
            
            # +( -> opened + 1 
            # +) -> closed + 1 

            if opened < n+1: 
                build(opened+1 , closed , res + "(")
            if closed < opened : 
                build(opened , closed+1 , res + ")")
        
        build(0 , 0 , "")

        return self.output