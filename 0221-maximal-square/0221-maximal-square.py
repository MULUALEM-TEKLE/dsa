class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows , cols = len(matrix) , len(matrix[0])
        @cache
        def explore(row , col) : 
            if not (0 <= row < rows) or not (0 <= col < cols) or matrix[row][col] == "0" : 
                return 0 
            
            return 1 + min(explore(row-1 , col) , explore(row , col-1) , explore(row-1 , col-1))
        
        max_side = 0 

        for r in range(rows) : 
            for c in range(cols) : 
                if matrix[r][c] == "1" : 
                    max_side = max(max_side , explore(r , c))
        
        return max_side ** 2 
