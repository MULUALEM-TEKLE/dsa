class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid) , len(grid[0])

        visited = set()
        def bfs(r , c) : 
            q = deque()
            q.append((r , c))
            visited.add((r , c))

            while q :
                row , col = q.popleft()
                directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
                for dr , dc in directions : 
                    nr , nc = row + dr , col + dc 
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr, nc) not in visited : 
                        q.append((nr , nc))
                        visited.add((nr , nc))

        def dfs(r , c) : 
            if r not in range(rows) or c not in range(cols) or grid[r][c] != "1" or (r , c) in visited : 
                return 

            visited.add((r , c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r , c+1)
            dfs(r , c-1)
        
        res = 0
        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == "1" and (r , c) not in visited : 
                    dfs(r , c)
                    res += 1 
        
        return res