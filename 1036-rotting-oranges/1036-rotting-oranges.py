class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]

        process = deque()
        fresh_oranges = 0

        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == 0 : 
                    continue 
                elif grid[r][c] == 1 : 
                    fresh_oranges += 1
                else : 
                    process.append((r , c))

        
        time = 0 

        while process and fresh_oranges : 
            for _ in range(len(process)) : 
                row , col = process.popleft()
                for dr , dc in directions : 
                    nr , nc = row + dr , col + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 : 
                        grid[nr][nc] = 2
                        fresh_oranges -= 1 
                        process.append((nr , nc))
            time +=  1 
        
        return time if fresh_oranges == 0 else -1

