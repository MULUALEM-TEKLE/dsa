class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9) : 
            s = set()
            for c in range(9) : 
                item = board[r][c]
                if item in s : 
                    return False
                elif item != "." : 
                    s.add(item) 
        for r in range(9) : 
            s = set()
            for c in range(9) : 
                item = board[c][r]
                if item in s : 
                    return False
                elif item != "." : 
                    s.add(item) 
        
        starts = [
            (0 ,0) , (0 , 3) , (0 , 6) , 
            (3 ,0) , (3 , 3) , (3 , 6) , 
            (6 ,0) , (6 , 3) , (6 , 6) , 
        ]

        for i,j in starts : 
            s = set()
            for row in range(i , i+3) : 
                for col in range(j , j+3) : 
                    item = board[row][col] 
                    if item in s : 
                        return False
                    elif item != "." : 
                        s.add(item)

        return True

