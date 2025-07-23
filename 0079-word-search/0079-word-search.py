class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board) , len(board[0])
        board_letter_counter = Counter()
        for r in range(rows) : 
            for c in range(cols) :
                board_letter_counter[board[r][c]] += 1 
        word_letter_counter = Counter(word)

        for letter,count in word_letter_counter.items() : 
            if board_letter_counter[letter] < count : 
                return False 
        
        if len(word) > rows*cols : 
            return False 
        
        if word_letter_counter[word[0]] > word_letter_counter[word[-1]] : 
            word = word[::-1]
        

        visited = set()
        def dfs(r , c , i) : 
            if i == len(word) : return True 
            if r not in range(rows) or c not in range(cols) or (r , c) in visited or word[i] != board[r][c] : 
                return False
            visited.add((r , c))
            res = dfs(r+1 , c , i+1) or dfs(r-1 , c , i+1) or dfs(r , c+1 , i+1) or dfs(r , c-1 , i+1)
            visited.remove((r , c))
            return res

        
        for r in range(rows) : 
            for c in range(cols) : 
                if board[r][c] == word[0] and (r , c) not in visited  : 
                    if dfs(r , c , 0) : return True 
        return False
