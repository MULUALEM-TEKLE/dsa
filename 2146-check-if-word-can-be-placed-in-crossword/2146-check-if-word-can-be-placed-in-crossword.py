'''
add all potiential starting positions to a queue 
process them with the word using dfs
if we can reach a border while the word is fully explored return true 
else return false
'''
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board) , len(board[0])
        word_len = len(word)

        hor_slots = []
        for row in range(rows) : 
            row_str = "".join(board[row])
            hor_slots.extend(row_str.split("#"))
        
        transposed_board = [
            [board[r][c] for r in range(rows)] for c in range(cols)
        ]

        vert_slots = []
        for col in range(cols) : 
            col_str = "".join(transposed_board[col])
            vert_slots.extend(col_str.split("#"))
        
        all_slots = vert_slots + hor_slots

        for slot in all_slots :
            if len(slot) == word_len : 
                forward_match = True 
                for i in range(word_len) : 
                    if slot[i] != " " and slot[i] != word[i] : 
                        forward_match = False
                        break
                if forward_match : return True 

                backward_match = True 
                for i in range(word_len) : 
                    if slot[i] != " " and slot[i] != word[word_len -1 -i] :
                        backward_match = False
                        break 
                if backward_match : return True 

        return False 

        

