class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows , cols = len(board) , len(board[0])
        visited = set()

        def dfs(r, c) : 
            if r not in range(rows) or c not in range(cols) or (r , c) in visited or board[r][c] == "." : 
                return 
            
            visited.add((r , c))
            dfs(r-1 , c)
            dfs(r+1 , c)
            dfs(r , c-1)
            dfs(r , c+1)

        ships = 0
        for r in range(rows) : 
            for c in range(cols) : 
                if board[r][c] == "X" and (r , c) not in visited : 
                    dfs(r , c) 
                    ships += 1 
        
        return ships