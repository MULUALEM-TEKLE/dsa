class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows , cols = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.pre = [[0]* cols for _ in range(rows)]
        # lets do a prefix sum on each row
        for r in range(rows) : 
            total = 0
            for c in range(cols) : 
                total += self.matrix[r][c]
                self.pre[r][c] = total
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1 , row2+1) : 
            if col1 == 0 : 
                total += self.pre[r][col2]
            else : 
                total += self.pre[r][col2] - self.pre[r][col1-1]
        return total

        # print(f"rows : {row1}->{row2}")
        # print(f"cols : {col1}->{col2}")
        # print(self.matrix)

'''
rows : 2->4
cols : 1->3
[
    [3, 0, 1, 4, 2], 
    [5, 6, 3, 2, 1], 
    [1, '*', '*', 1, 5], 
    [4, '*', '*', 1, 7], 
    [1, '*', '*', 0, 5]]
'''


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)