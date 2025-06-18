# from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board) , len(board[0])
        path = set()

        board_char_counts = {}
        for r in range(rows):
            for c in range(cols):
                board_char_counts[board[r][c]] = board_char_counts.get(board[r][c] , 0) + 1 

        word_char_counts = {}

        for char in word : 
            word_char_counts[char] = word_char_counts.get(char , 0) + 1
            
        for char, count in word_char_counts.items():
            if char not in board_char_counts or board_char_counts[char] < count:
                return False

        # Also, for an edge case: if the word is longer than the total number of cells, it can't exist.
        if len(word) > rows * cols:
            return False

        def dfs(r , c , i) : 
            if i == len(word)  : 
                return True 
            
            if r not in range(rows) or c not in range(cols) or word[i] != board[r][c] or (r , c) in path : 
                return False

            
            path.add((r , c))
            res = dfs(r+1 , c , i+1) or dfs(r-1 , c , i+1) or dfs(r , c+1 , i+1) or dfs(r , c-1 , i+1)
            path.remove((r ,c))
            return res
        
        res = False

        for r in range(rows): 
            for c in range(cols) : 
                if board[r][c] == word[0] : 
                    res = res or dfs(r , c , 0)
                    if res : 
                        return True
        
        return False