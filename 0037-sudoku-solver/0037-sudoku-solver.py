class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = 9

        rows_used = [set() for _ in range(N)]
        cols_used = [set() for _ in range(N)]
        boxes_used = [set() for _ in range(N)] # There are 9 3x3 boxes, indexed 0-8

        # --- 2. Pre-populate Trackers based on the initial board ---
        # Iterate through the given board and fill the sets with existing numbers.
        for r in range(N):
            for c in range(N):
                if board[r][c] != ".":
                    num = board[r][c]
                    box_idx = (r // 3) * 3 + (c // 3) # Calculate the 3x3 box index
                    
                    rows_used[r].add(num)
                    cols_used[c].add(num)
                    boxes_used[box_idx].add(num)

        def solve(r , c) : 
            if c == N : return solve(r+1 , 0)
            if r == N : return True
            if board[r][c] != "."  : return solve(r , c+1)
            for num_char in '123456789' : 
                box_idx = (r // 3) * 3 + (c // 3)
                if (num_char not in rows_used[r] and
                    num_char not in cols_used[c] and
                    num_char not in boxes_used[box_idx]):

                    board[r][c] = num_char 

                    rows_used[r].add(num_char)
                    cols_used[c].add(num_char)
                    boxes_used[box_idx].add(num_char)
                   
                    if solve(r , c+1) : 
                        return True

                    board[r][c] = "."
                    rows_used[r].remove(num_char)
                    cols_used[c].remove(num_char)
                    boxes_used[box_idx].remove(num_char)
            return False
        
        def isValid(r , c , num) : 
            for i in range(N) : 
                if board[r][i] == num or board[i][c] == num : 
                    return False
            start_row , start_col = 3 *(r//3) , 3 *(c//3)
            for i in range(start_row , 3+start_row) : 
                for j in range(start_col , 3+start_col) : 
                    if board[i][j] == num : return False
            return True
        
        solve(0 , 0)