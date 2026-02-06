class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split('/')
        print(stack)
        res = []
        for p in stack : 
            if p == "." or p == "" : 
                continue 
            elif p == ".." : 
                if res : res.pop() 
            else : 
                res.append(p)
            
        return "/" + "/".join(res) 