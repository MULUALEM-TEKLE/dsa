class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        dxn = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
        visited = set()

        def bfs(r , c) : 
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            island_area = 1
            while q: 
                row , col = q.popleft()
                for dr,dc in dxn : 
                    r , c = row + dr , col + dc
                    if r in range(rows) and c in range(cols) and (r , c) not in visited and grid[r][c] == 1 : 
                        q.append((r, c))
                        visited.add((r , c))
                        island_area += 1 
            return island_area
            

        area = 0
        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == 1 and (r , c) not in visited: 
                    area = max(area , bfs(r , c))
        return area