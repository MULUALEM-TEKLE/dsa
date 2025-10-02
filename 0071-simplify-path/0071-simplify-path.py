class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        path_stack = []
        print(split_path)

        for p in split_path : 
            if p == ".."  : 
                if path_stack : path_stack.pop()
                continue
            elif p == "/" or p == "" or p == ".": 
                continue
            else : 
                path_stack.append(p)
        
        return  '/'+"/".join(path_stack)