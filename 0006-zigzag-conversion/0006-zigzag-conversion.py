class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        rows = numRows
        if rows == 1 : 
            return s
        mat = [[] for _ in range(rows+1)] 
        d = 1
        i = 0
        print(mat)
    
        for c in s : 
            mat[i].append(c)
            if i == 0 : 
                d = 1
            elif i == rows-1 : 
                d = -1
            i += d
        
        res = ''
        for r in mat : 
            res += ''.join(r)
        
        return res


