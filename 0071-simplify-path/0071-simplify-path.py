class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")

        stack = []

        for file in path : 
            if file == ".." : 
                if stack : stack.pop()
            elif file == "." or not file : 
                continue 
            else : 
                stack.append(file)
        
        return "/" + "/".join(stack)