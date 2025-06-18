class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board) , len(board[0])
        path = set()

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