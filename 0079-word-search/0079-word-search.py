class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board) , len(board[0])

        if len(word) > rows * cols : 
            return False
        
        word_counter = Counter(word)
        board_counter = defaultdict(int)

        for r in range(rows) : 
            for c in range(cols) : 
                board_counter[board[r][c]] += 1 
        
        for letter,count in word_counter.items() : 
            if count > board_counter[letter] : 
                return False

        visited = set()
        def dfs(r , c , i) : 
            if r not in range(rows) or c not in range(cols) or (r , c) in visited or board[r][c] != word[i] : 
                return False
            
            if i == len(word) - 1 : 
                return True

            visited.add((r , c))
          
            res = dfs(r+1 , c , i+1) or dfs(r-1 , c , i+1) or dfs(r , c+1 , i+1) or dfs(r , c-1 , i+1) 

            visited.remove((r , c))

            return res

        for r in range(rows) : 
            for c in range(cols) : 
                if board[r][c] == word[0] and (r , c) not in visited : 
                    if dfs(r , c , 0) : 
                        return True
        return False