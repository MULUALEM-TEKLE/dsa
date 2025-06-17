class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board) , len(board[0])
        directions = [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]]
        res = False

        def bfs(r , c) : 
            stack = []
            visited = set()
            stack.append((r , c , 0 , {(r , c)}  ))
            visited.add((r , c))
            

            while stack : 
                row , col , idx , visited  = stack.pop()

                if idx == len(word) - 1 : 
                    return True
            
                for dr,dc in directions : 
                    r , c = row + dr , col + dc
                    if r in range(rows) and c in range(cols) and (r , c) not in visited and board[r][c] == word[idx + 1]:   
                        new_visited = visited.copy()
                        new_visited.add((r , c))
                        stack.append((r , c , idx + 1 , new_visited ))
                       
            return False


        for r in range(rows) : 
            for c in range(cols) : 
                if board[r][c] == word[0]: 
                   res = res or bfs(r,c )

        
        return res
