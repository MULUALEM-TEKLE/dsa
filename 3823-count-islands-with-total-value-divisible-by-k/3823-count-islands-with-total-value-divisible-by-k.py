class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid) , len(grid[0])
        visited = set()

        def bfs(r , c) : 
            q = deque()
            q.append((r , c))
            visited.add((r , c))
            total_area = grid[r][c]

            while q : 
                row , col = q.popleft()

                directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]

                for dr , dc in directions : 
                    r , c = row + dr , col + dc 

                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] != 0 : 
                        q.append((r , c))
                        visited.add((r , c))
                        total_area += grid[r][c]
            return 1 if total_area % k == 0 else 0
        
        res = 0
        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] != 0 and (r , c) not in visited : 
                    res += bfs(r , c)

        return res
