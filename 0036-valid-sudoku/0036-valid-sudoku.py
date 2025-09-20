class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = cols = 9

        for row in range(rows) : 
            bucket = set()
            for col in range(cols) :  
                if board[row][col] == "." : continue 
                if board[row][col] in bucket : 
                    print("a")
                    return False
                bucket.add(board[row][col])
        
        for col in range(cols) :  
            bucket = set()
            for row in range(rows) : 
                if board[row][col] == "." : continue 
                if board[row][col] in bucket : 
                    print("b")
                    return False
                bucket.add(board[row][col])
        
        starts = [
            [0,0] , [0,3] , [0,6] , 
            [3,0] , [3,3] , [3,6] , 
            [6,0] , [6,3] , [6,6] , 
            ]

        for i,j in starts : 
            bucket = set()
            for row in range(i , i+3) : 
                for col in range(j , j+3) : 
                    if board[row][col] == "." : continue 
                    if board[row][col] in bucket : 
                        print("c")
                        return False
                    bucket.add(board[row][col])
            # print(bucket)
        
        return True 