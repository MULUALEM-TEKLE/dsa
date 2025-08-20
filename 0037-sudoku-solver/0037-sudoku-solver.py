class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = 9
        rows_used = [set() for i in range(N)]
        cols_used = [set() for i in range(N)]
        boxes_used = [set() for i in range(N)]

        for r in range(N) : 
            for c in range(N) : 
                box_idx = (r//3) * 3 + (c // 3)
                if board[r][c] != "." : 
                    rows_used[r].add(board[r][c])
                    cols_used[c].add(board[r][c])
                    boxes_used[box_idx].add(board[r][c])

        def solve(r , c) : 
            if c == N : 
                return solve(r+1 , 0)
            if r == N : 
                return True 
            
            if board[r][c] != "." : 
                return solve(r , c+1)
            
            for num in '123456789' : 
                box_idx = (r//3) * 3 + (c // 3)
                if num not in rows_used[r] and num not in cols_used[c] and num not in boxes_used[box_idx] : 
                    rows_used[r].add(num)
                    cols_used[c].add(num)
                    boxes_used[box_idx].add(num)

                    board[r][c] = num

                    if solve(r , c+1) : return True

                    board[r][c] = "."

                    rows_used[r].remove(num)
                    cols_used[c].remove(num)
                    boxes_used[box_idx].remove(num)
            return False
        
        solve(0 , 0)

        

