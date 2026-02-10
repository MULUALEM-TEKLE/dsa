class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        directions = [[1 , 0] , [-1 , 0] , [0 , 1 ] , [0 , -1]]
        fresh_count = 0 
        rotten = deque()
        visited = set()
        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == 1 : 
                    fresh_count += 1 
                elif grid[r][c] == 2 : 
                    rotten.append((r , c))
                    visited.add((r , c))
        time = 0
        while rotten and fresh_count : 
            for _ in range(len(rotten)) : 
                r , c = rotten.popleft()
                for dr , dc in directions : 
                    nr , nc = r+dr , c+dc
                    if nr in range(rows) and nc in range(cols) and (nr , nc) not in visited and grid[nr][nc] == 1 : 
                        fresh_count -= 1 
                        grid[nr][nc] = 2 
                        rotten.append((nr , nc))
                        visited.add((nr , nc))
            time += 1 
        
        if fresh_count == 0 : 
            return time 
        return -1
        
