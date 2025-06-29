class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix : return []

        start_row ,end_row , start_col , end_col = 0 , len(matrix) , 0 , len(matrix[0])
        res = []
        while start_row < end_row or start_col < end_col : 
            if start_row < end_row : res.extend([matrix[start_row][i] for i in range(start_col , end_col)])
            start_row += 1
            if start_col < end_col :  res.extend([matrix[i][end_col-1] for i in range(start_row , end_row)])
            end_col -= 1
            if start_row < end_row : res.extend([matrix[end_row-1][i] for i in range(end_col-1 , start_col-1, -1)])
            end_row -= 1
            if start_col < end_col : res.extend([matrix[i][start_col] for i in range(end_row-1 , start_row-1 , -1)])
            start_col += 1
        return res



                
            