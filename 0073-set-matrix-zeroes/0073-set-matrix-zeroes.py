class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows , cols = len(matrix) , len(matrix[0])
        def mark_zero(row , col) : 
            for i in range(rows) : 
                matrix[i][col] = 0
            for i in range(cols) : 
                matrix[row][i] = 0 
        
        cells_to_process = []
        for r in range(rows): 
            for c in range(cols) : 
                if matrix[r][c] == 0 : 
                    cells_to_process.append((r , c))
        
        for row , col in cells_to_process : 
            mark_zero(row , col)
