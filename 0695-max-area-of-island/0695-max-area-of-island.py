class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]

        visited = set()
        self.max_area = 0

        def bfs(r , c) : 
            q = deque([(r , c)])
            visited.add((r , c))

            area = 1

            while q : 
                row , col = q.popleft()
                for dr , dc in directions : 
                    nr , nc = row + dr , col + dc 
                    if nr in range(rows) and nc in range(cols) and (nr , nc ) not in visited and grid[nr][nc] == 1 : 
                        area += 1 
                        visited.add((nr , nc))
                        q.append((nr , nc))

            self.max_area = max(self.max_area , area) 
        

        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == 1 and (r , c) not in visited : 
                    bfs(r , c)
        

        return self.max_area