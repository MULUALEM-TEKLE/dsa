class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        ne = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
        visited = set()
        area = 0

        def bfs(r , c) : 
            island_area = 1
            q = deque()
            q.append((r , c))
            visited.add((r , c))

            while q : 
                row , col = q.popleft()
                for dr , dc in ne : 
                    nr, nc = row+dr , col+dc
                    if nr in range(rows) and nc in range(cols) and (nr , nc) not in visited and grid[nr][nc] == 1 : 
                        q.append((nr , nc))
                        visited.add((nr , nc))
                        island_area += 1 
            return island_area
        
        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == 1 and (r , c) not in visited : 
                    area = max(area , bfs(r , c))
        
        return area