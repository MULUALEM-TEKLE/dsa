class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # if numRows == 1 : return [[1]]
        # if numRows == 2 : return [[1] , [1 , 1]]
        res = [[1]]
        for i in range(1 , numRows) : 
            cur = [1]
            prev_level = -1
            for j in range(len(res[prev_level])-1) : 
                cur.append(res[prev_level][j] + res[prev_level][j+1])
            cur.append(1)
            res.append(cur)
        return res 
            