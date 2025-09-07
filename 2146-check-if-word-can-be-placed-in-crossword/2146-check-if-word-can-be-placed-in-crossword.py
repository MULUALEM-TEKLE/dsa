'''
add all potiential starting positions to a queue 
process them with the word using dfs
if we can reach a border while the word is fully explored return true 
else return false
'''
# class Solution:
#     def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
#         rows , cols = len(board) , len(board[0])
#         word_len = len(word)

#         hor_slots = []
#         for row in range(rows) : 
#             row_str = "".join(board[row])
#             hor_slots.extend(row_str.split("#"))
        
#         transposed_board = [
#             [board[r][c] for r in range(rows)] for c in range(cols)
#         ]

#         vert_slots = []
#         for col in range(cols) : 
#             col_str = "".join(transposed_board[col])
#             vert_slots.extend(col_str.split("#"))
        
#         all_slots = vert_slots + hor_slots

#         for slot in all_slots :
#             if len(slot) == word_len : 
#                 forward_match = True 
#                 for i in range(word_len) : 
#                     if slot[i] != " " and slot[i] != word[i] : 
#                         forward_match = False
#                         break
#                 if forward_match : return True 

#                 backward_match = True 
#                 for i in range(word_len) : 
#                     if slot[i] != " " and slot[i] != word[word_len -1 -i] :
#                         backward_match = False
#                         break 
#                 if backward_match : return True 

#         return False 

        

from typing import List

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        word_len = len(word)
        
        # All possible directions for word placement.
        # (dr, dc) where dr is change in row, dc is change in column.
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up

        def check_direction(r, c, dr, dc):
            """
            Checks if the word can be placed starting from (r, c) in the direction (dr, dc).
            """
            # Check the cell before the start of the word. It must be blocked or out of bounds.
            start_r, start_c = r - dr, c - dc
            if 0 <= start_r < rows and 0 <= start_c < cols and board[start_r][start_c] != '#':
                return False

            # Check if the length of the slot is exactly the length of the word.
            # We traverse the board in the given direction.
            end_r, end_c = r, c
            path_len = 0
            while 0 <= end_r < rows and 0 <= end_c < cols and board[end_r][end_c] != '#':
                path_len += 1
                end_r += dr
                end_c += dc
            
            if path_len != word_len:
                return False

            # Check the cell after the end of the word. It must also be blocked or out of bounds.
            if 0 <= end_r < rows and 0 <= end_c < cols and board[end_r][end_c] != '#':
                return False

            # Now, check if the word's characters can be placed in this slot.
            for i in range(word_len):
                cur_r, cur_c = r + i * dr, c + i * dc
                if board[cur_r][cur_c] != ' ' and board[cur_r][cur_c] != word[i]:
                    return False
            
            # If all conditions are met, the word can be placed.
            return True

        # Check every possible cell on the board as a potential starting point.
        for r in range(rows):
            for c in range(cols):
                # We only need to start a check if the current cell is not blocked.
                if board[r][c] != '#':
                    # For each starting cell, check all four directions.
                    for dr, dc in directions:
                        if check_direction(r, c, dr, dc):
                            return True
        
        # If no valid placement is found after checking all possibilities, return False.
        return False