class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board) , len(board[0])
        start_pos = []
        for r in range(rows) : 
            for c in range(cols) : 
                if board[r][c] == word[0] : 
                    start_pos.append((r ,c))
        visited = set()
        def dfs(r , c , idx) : 
            if len(word) == idx : 
                return True
            if r not in range(rows) or c not in range(cols) or board[r][c] != word[idx] or (r , c) in visited: 
                return False
            visited.add((r , c))
            dxn = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
            res = False 
            for dr,dc in dxn : 
                res = res or dfs(r+dr , c+dc , idx+1)
            visited.remove((r, c))
            return res

        
        for r,c in start_pos : 
            if dfs(r , c , 0) : 
                return True 
        return False