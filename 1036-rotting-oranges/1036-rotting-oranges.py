class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])

        q = deque()
        fresh_oranges = 0

        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == 2 : 
                    q.append((r , c))
                if grid[r][c] == 1 : 
                    fresh_oranges +=1 
        minutes = 0
        while q and fresh_oranges > 0: 
            for _ in range(len(q)) : 
                row , col = q.popleft()
                dxn = [[1 ,0] , [-1 , 0] , [0 , 1] , [0 , -1]]
                for dr, dc in dxn : 
                    r , c = row + dr , col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 : 
                        grid[r][c] = 2
                        q.append((r , c))
                        fresh_oranges -= 1 
            
            if q : 
                minutes += 1
        
        if fresh_oranges == 0 : 
            return minutes 
        else : 
            return -1