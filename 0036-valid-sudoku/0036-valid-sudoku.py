class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9 
        for r in range(N) : 
            s = set()
            for c in range(N) : 
                if board[r][c] == "." : continue 
                if board[r][c] in s : return False 
                s.add(board[r][c])
            
        for c in range(N) : 
            s = set()
            for r in range(N) : 
                if board[r][c] == "." : continue 
                if board[r][c] in s : return False 
                s.add(board[r][c])
        
        start = [
            [0 , 0] , [0 , 3] , [0 , 6] , 
            [3 , 0] , [3 , 3] , [3 , 6] , 
            [6 , 0] , [6 , 3] , [6 , 6] , 
            ]
        
        for i,j in start : 
            s = set()
            for r in range(i , i+3) : 
                for c in range(j , j+3) : 
                    if board[r][c] == "." : continue 
                    if board[r][c] in s : return False 
                    s.add(board[r][c])
        
        return True