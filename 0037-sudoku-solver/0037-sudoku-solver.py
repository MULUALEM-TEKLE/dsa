from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = 9

        # --- 1. Initialize State Trackers ---
        # These will keep track of which numbers are used in each row, column, and 3x3 box.
        # Using sets allows for O(1) average time complexity for add, remove, and check operations.
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

        # --- The Recursive Backtracking Solver Function ---
        def solve(r: int, c: int) -> bool:
            # Base Case 1: If we've moved past the last column (c == N),
            # it means the current row 'r' is completely filled.
            # Move to the first column of the next row (r+1).
            if c == N:
                return solve(r + 1, 0)

            # Base Case 2: If we've moved past the last row (r == N),
            # it means the entire board has been successfully filled.
            # The puzzle is solved!
            if r == N:
                return True

            # If the current cell is already filled (not '.'),
            # we don't need to try filling it. Just move to the next cell.
            if board[r][c] != ".":
                return solve(r, c + 1)

            # --- Backtracking Logic for Empty Cells ('.') ---
            # Try placing numbers from '1' to '9' in the current empty cell.
            for num_char in '123456789':
                # Calculate the current 3x3 box index
                box_idx = (r // 3) * 3 + (c // 3)

                # --- Optimized isValid Check (O(1) lookup) ---
                # Check if 'num_char' is already used in the current row, column, or box.
                if (num_char not in rows_used[r] and
                    num_char not in cols_used[c] and
                    num_char not in boxes_used[box_idx]):
                    
                    # If valid, place the number on the board (tentatively)
                    board[r][c] = num_char
                    
                    # --- Update Trackers (Add the number) ---
                    rows_used[r].add(num_char)
                    cols_used[c].add(num_char)
                    boxes_used[box_idx].add(num_char)

                    # Recursively try to solve the rest of the board from the next cell.
                    if solve(r, c + 1):
                        return True # If the recursive call returns True, a solution is found!

                    # --- Backtrack (Remove the number and revert board/trackers) ---
                    # If the recursive call did not lead to a solution,
                    # undo the current choice and try the next number.
                    board[r][c] = "." # Revert the board cell
                    
                    # --- Update Trackers (Remove the number) ---
                    rows_used[r].remove(num_char)
                    cols_used[c].remove(num_char)
                    boxes_used[box_idx].remove(num_char)
            
            # If no number from '1' to '9' leads to a solution for this cell,
            # then the current path is invalid. Backtrack further up the recursion stack.
            return False

        # Start the solving process from the top-left corner (0, 0).
        solve(0, 0)

