class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        dxn = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]

        rotten = deque()
        fresh = 0

        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == 2 : 
                    rotten.append((r, c))
                elif grid[r][c] == 1 : 
                    fresh += 1 
        minutes = 0
        while rotten and fresh > 0 : 
            for _ in range(len(rotten)) : 
                row , col = rotten.popleft()
                for dr , dc in dxn : 
                    r , c = row + dr , col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 : 
                        grid[r][c] = 2 
                        fresh -= 1
                        rotten.append((r , c))
                        
            minutes += 1   
        
        if fresh == 0 : 
            return minutes 
        else : 
            return -1