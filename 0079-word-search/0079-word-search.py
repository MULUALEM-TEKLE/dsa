class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board) , len(board[0])

        visited = set()

        def dfs(r , c , i) : 
            if r not in range(rows) or c not in range(cols) or (r , c) in visited or board[r][c] != word[i] : 
                return False
            
            # success condition
            if i == len(word) - 1 : 
                return True

            visited.add((r , c))
            # recursive
            res = dfs(r+1 , c , i+1) or dfs(r-1 , c , i+1) or dfs(r , c+1 , i+1) or dfs(r , c-1 , i+1) 
            
            visited.remove((r , c))

            return res

        

        for r in range(rows) : 
            for c in range(cols) : 
                if board[r][c] == word[0] and (r , c) not in visited : 
                    if dfs(r , c , 0) : 
                        return True
        return False