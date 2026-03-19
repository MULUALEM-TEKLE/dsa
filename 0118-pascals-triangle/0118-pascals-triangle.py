class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1 : return [[1]]
        if numRows == 2 : return [[1] , [1 , 1]]
        res = [[1] , [1 , 1]]
        for i in range(2 , numRows) : 
            cur = []
            for j in range(len(res[i-1])-1) : 
                cur.append(res[i-1][j] + res[i-1][j+1])
            res.append([1] + cur +[1])
        return res 
            