class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        nei = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
        visited = set()
        count = 0

        def bfs(r , c ) : 
            q = deque()
            q.append((r , c))
            visited.add((r , c))

            while q : 
                row , col = q.popleft()

                for dr , dc in nei : 
                    nr , nc = row+dr , col+dc
                    if nr in range(rows) and nc in range(cols) and (nr , nc) not in visited and grid[nr][nc] == "1" : 
                        q.append((nr, nc))
                        visited.add((nr , nc))
        
        for r in range(rows) : 
            for c in range(cols) : 
                if (r , c) not in visited and grid[r][c] == "1" :
                    bfs(r , c)
                    count += 1 
        
        return count
