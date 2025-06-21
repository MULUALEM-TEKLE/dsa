class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        board_letters_counter = Counter() 
        for r in range(rows) : 
            for c in range(cols) : 
                board_letters_counter[board[r][c]] += 1 
        word_letter_counter = Counter(word)
        
        for char, count in word_letter_counter.items(): 
            if board_letters_counter[char] < count : 
                return False
        
        if len(word) > rows * cols : 
            return False 

        def dfs(r , c , i) : 
            if i == len(word) : 
                return True
            
            if r not in range(rows) or c not in range(cols) or board[r][c] != word[i] or (r , c) in visited : 
                return False 
            
            visited.add((r,c))
            res = dfs(r+1 , c , i+1) or dfs(r-1 , c , i+1) or dfs(r , c+1 , i+1) or dfs(r , c-1 , i+1) 
            visited.remove((r , c))
            return res

        is_word_there = False
        for r in range(rows) : 
            for c in range(cols) : 
                if board[r][c] == word[0] and (r, c) not in visited : 
                    is_word_there = is_word_there or dfs(r , c , 0)
                    if is_word_there : 
                        return True
        return False