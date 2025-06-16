class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid : 
            return 0

        visited = set()
        rows , cols = len(grid) , len(grid[0])
        island_area = 0

        def bfs(r , c) : 
            q = deque()
            q.append((r , c))
            visited.add((r , c))
            area = 1

            while q : 
                row , col = q.popleft()
                directions = [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]]

                for dr,dc in directions : 
                    r , c = row + dr , col + dc

                    if r in range(rows) and c in range(cols) and (r , c) not in visited and grid[r][c] == 1 : 
                        q.append((r , c))
                        visited.add((r , c))
                        area += 1
            return area


        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == 1 and (r , c) not in visited : 
                    print("calling bfs")
                    island_area = max(island_area ,bfs(r , c))
        
        return island_area
        # return 0