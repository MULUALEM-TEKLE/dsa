class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9 

        for r in range(N) : 
            s = set()
            for c in range(N) : 
                cell = board[r][c]
                if cell == "." : 
                    continue
                if cell in s : return False
                s.add(cell)
        
        for c in range(N) : 
            s = set()
            for r in range(N) : 
                cell = board[r][c]
                if cell == "." : 
                    continue
                if cell in s : return False
                s.add(cell)
        
        start = [
            [0 , 0] , [0 , 3] , [0 , 6] , 
            [3 , 0] , [3 , 3] , [3 , 6] , 
            [6 , 0] , [6 , 3] , [6 , 6] , 

        ]

        for r , c in start : 
            s = set()
            for row in range(r , r+3) : 
                for col in range(c , c+3) : 
                    cell = board[row][col]
                    if cell == "." : continue 
                    if cell in s : return False 
                    s.add(cell)

        return True