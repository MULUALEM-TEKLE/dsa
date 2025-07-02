def register_edges(board) : 
    left , right , top , bottom = 0 , len(board[0]) , 0 , len(board)
    edges = set()
    for i in range(left , right) : 
        edges.add((top , i))
        edges.add((bottom-1 , i))
    for i in range(top+1 , bottom-1) : 
        edges.add((i, left))
        edges.add((i , right-1 ))
    return edges
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        edges = register_edges(board)
        visited = set()
        def bfs(r , c) :
            q = deque()
            visited.add((r , c))
            q.append((r , c))
            mark = set()
            mark.add((r , c))
            safe = True

            while q : 
                row , col = q.popleft()
                if (row , col) in edges : 
                    safe = False
                directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]] 
                for dr , dc in directions : 
                    r , c = row + dr , col + dc 
                    if r in range(rows) and c in range(cols) and (r,c) not in visited and board[r][c] == "O" : 
                        mark.add((r,c))
                        q.append((r , c))
                        visited.add((r , c))
            if safe : 
                for row,col in mark : 
                    board[row][col] = "X"

        rows , cols = len(board) , len(board[0])

        for r in range(rows) : 
            for c in range(cols) : 
                if board[r][c] == "O" and (r , c) not in visited and (r , c) not in edges  : 
                    bfs(r , c)
        
        

        